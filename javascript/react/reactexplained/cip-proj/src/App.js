import React, { useState, useEffect } from "react";

import {
  BrowserRouter as Router,
  Routes,
  Route,
  Navigate,
  useParams,
} from "react-router-dom";

// pachetul react-storate-hooks nu mai poate fi instalat cu ultima varianta node
// import { useLocalStorage } from "react-storage-hooks"
/*
  Pentru a compensa, se foloseste obiectul localStorage cu metodele:
   - getItem("key")
   - setItem("key", string)
  Daca am ceva stocat in localStorage la cheia data voi obtine string-ul
  Acesta trebuie transformat in json: JSON.parse(string)

  De fiecare data cand modific ceva, vreau sa actualizez si localStorage.
  Pot face asta printr-un hook useEffect(functie_actualizare, [posts]) care
  va apela functie_actualizare la fiecare modificare a variabilei care trebuie
  salvata in localStorage.
  Transformare obiect -> string: JSON.stringify(obiect)

*/

import { signInWithEmailAndPassword, signOut } from "firebase/auth";
import { set, ref, push, onValue, update, remove } from "firebase/database";

import logo from './logo.svg';
import './App.css';

import UserContext from "./context/UserContext";

import Header from "./components/Header";
import Posts from  "./components/Posts";
import Post from "./components/Post";
import NotFound from "./components/NotFound";
import PostForm from "./components/PostForm";
import Message from "./components/Message";
import Login from "./components/Login";
import { firebaseauth, firebasedb } from "./firebase";


const App = (props) => {

  const [posts, setPosts] = useState([]);
  const [user, setUser] = useState({});

  useEffect(() => {
    //console.log("useEffect - preluare date");
    const postsRef = ref(firebasedb, '/posts/'+user.uid);

    onValue(postsRef, (snapshot) => {
      const dbPosts = snapshot.val();
      //console.log("in onValue firedb, dbPosts:", dbPosts );

      const newStatePosts = [];
      for (let post in dbPosts) {
        console.log("in for: post: ", post);
        newStatePosts.push({
          key: post,
          slug: dbPosts[post].slug,
          title: dbPosts[post].title,
          content: dbPosts[post].content,
        });
      }
      console.log("onValue. newStatePosts: ", newStatePosts);
      setPosts(newStatePosts);
    });
  }, [user]); //calling at each login/logout to ensure proper data are shown

  const [message, setMessage] = useState(null);
  const [messageInfo, setMessageInfo] = useState("");
  const setFlashMessage = (message, messageInfo) => {
    setMessage(message);
    setMessageInfo(messageInfo);
    setTimeout(() => {
      setMessage(null);
      setMessageInfo("");
    }, 1600);
  }

  const getNewSlugFromTitle = (title) => {
    return(encodeURIComponent(title.toLowerCase().split(" ").join("-")));
  }

  const addNewPost = (post) => {
    //post.id = posts.length + 1;
    //const postsRef = firebasedb.ref("posts");
    post.slug = getNewSlugFromTitle(post.title);
    delete post.key;
    //setPosts([...posts, post]); // for local storage
    console.log("user.uid: ", user.uid);
    push(ref(firebasedb, "/posts/"+user.uid), post);
    setFlashMessage(`saved`);
  }

  const updatePosts = (post) => {
    //const param = useParams(); //Nu se poate apela aici. Doar in componente sau hook-uri
    console.log("updatePosts start. post = ", post);

    const updates = {};
    updates["/posts/" + user.uid + "/" + post.key] = {
      slug: getNewSlugFromTitle(post.title),
      title: post.title,
      content: post.content,
    }

    console.log("updates =", updates);
    update(ref(firebasedb, "/posts/" + user.uid + "/" + post.key), {
      slug: getNewSlugFromTitle(post.title),
      title: post.title,
      content: post.content,
    });
    //<Navigate to= "/">
    setFlashMessage(`saved`);
  }

  const deletePost = (post) => {
    if (window.confirm("Delete this post?")) {
      remove(ref(firebasedb, "/posts/" + user.uid + "/" + post.key));
      setFlashMessage('deleted');
    }
  }

  //const f_b_a = firebase;
  //console.log("f_b_a", f_b_a)


  const onLogin = (email, password) => {
    signInWithEmailAndPassword(firebaseauth, email, password)
      .then((userCredential) => {
        const user = userCredential.user;
        console.log("user", user);
        setUser({
          uid: user.uid,
          email: user.email,
          isAuthenticated: true,
        });
        console.log("login OK teo", user);
      })
      .catch((error) => {
        const errorCode = error.code;
        const errorMessage = error.message;
        console.log("errorCode: ", errorCode, "errorMessage: ", errorMessage);
        setFlashMessage(`loginerror`, errorMessage);
      });
  };

  const onLogout = () => {
    signOut(firebaseauth)
      .then(() => {
        setUser({
          uid: undefined,
          email: undefined,
          isAuthenticated: false });
        setPosts([]); //when getting info from firebase, see it only if auth
      })
      .catch((error) => console.log(error))
  }

  return (
      <div className="App">
        <Router>
          <UserContext.Provider value={{ user, onLogin, onLogout }}>
            <Header />
            {message && <Message type={message} info={messageInfo} />}
            <Routes>
              <Route path="/" element=<Posts posts={posts} deletePost={deletePost} /> />
              <Route path="/post/:postSlug" element=<Post posts={posts} /> />

              <Route path="/new"
                element={ user.isAuthenticated ?
                  <PostForm addNewPost={addNewPost} /> :
                  <Navigate to="/" />
                }
              />

              <Route path="/edit/:postSlug"
                element={ user.isAuthenticated ?
                  <PostForm posts={posts} updatePosts={updatePosts} /> :
                  <Navigate to="/" />
                }
              />

              <Route path="/login"
                element={! user.isAuthenticated ? <Login onLogin={onLogin} /> :
                <Navigate to="/" />}
              />

              <Route path="*" element=<NotFound /> />
            </Routes>
          </UserContext.Provider>
        </Router>
      </div>
  );
}

export default App;
