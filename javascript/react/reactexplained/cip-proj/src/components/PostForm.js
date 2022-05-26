import React, { useState, useEffect, useRef } from "react";
import { Navigate, useParams } from "react-router-dom";

import { Quill, useQuill } from "react-quilljs";
import 'quill/dist/quill.snow.css'; // Add css for snow theme

//De analizat mai mult sintaxa.
//in consola apar doar numere PARE - DE CE?
/*
 Definesc o functie in care declar o alta functie si o si apelez.
 Rezultatul acestor operatii ete functia 'afiseazaLaRender'
 care este atribuit variabilei 'afiseazaLaRender'.
*/

const afiseazaLaRender = (function() {
    let nr_rerender = 0;
    console.log("Fisier PostForm: afiseazaLaRender, nr_rerender = ", nr_rerender);
    function afiseazaLaRender() {
        console.log("PostForm. nr_rerender: ", nr_rerender);
        return nr_rerender++;
    }
    return afiseazaLaRender;
}());


const PostForm = (props) => {

  const params = useParams();
  const posts = props.posts;
  const addNewPost = props.addNewPost;
  const updatePost = props.updatePosts;

  let propsPost = {};
  if(updatePost) {
    propsPost = posts.find((p) => p.slug === params.postSlug)
    if(propsPost === undefined) {
      //la update se reincarca PostForm - pana la save = true
      //daca schimbam titlul, cu slug cu tot, slug-ul este diferit de cel din Posts
      //care a ramas la varianta initiala.
      //acest if face sa nu crape pagina la intializare mai jos: titlu si continut
      propsPost = {key: null, slug: "", title: "", content: ""};
    }
  } else {
    propsPost = {key: null, slug: "", title: "", content: ""};
  }

  //DEBUG - martor render de mai multe ori
  //console.log("PostForm START. propsPost:", propsPost); // apelat de mai multe ori cand se afiseaz pagina  - de ce? din 2 in 2 de obicei. de ce nu prind si secv inpare?
  afiseazaLaRender();

  //const [post, setPost] = useState({...propsPost});
  const [title, setTitle] = useState(propsPost.title);
  const [content, setContent] = useState(propsPost.content);
  const [saved, setSaved] = useState(false);

  console.log("PostForm. title = ", title)

  //console.log("PostForm: propsPost = ", propsPost);

  const { quill, quillRef } = useQuill();
  //### With onChange Handler - from react-quilljs readme examples
  useEffect(() => {
    if (quill) {
      console.log("if(quill) useEffect: content =", content)

      if(typeof(content) === 'string') {
        //quill.clipboard.dangerouslyPasteHTML(content);
        quill.setText(content);
      } else {
        quill.setContents(content);
      }

      quill.on('text-change', (delta, oldDelta, source) => {
        /*
        console.log('Text change!');
        console.log(quill.getText()); // Get text only
        console.log(quill.getContents()); // Get delta contents
        console.log(quill.root.innerHTML); // Get innerHTML using quill
        console.log(quillRef.current.firstChild.innerHTML); // Get innerHTML using quillRef
        */
        //console.log("quill on: event content:", content); // nu vad aici 'content' din parinte
        setContent(quill.getContents());
      });
    }
  }, [quill]);

  //2 referinte - una pentru post, alta pentru quill
  //2 useEffect - prima se va apela cand se modifica propsPost
  //            - a doua se va apela cand se
  //Ambele au ca rol actualizarea  continutului controalelor cand sunt in edit
  //si trec in new - trebuie sa se stearga continutul din edit.
  //Fara acestea, daca din Edit trec in "New Post" titlul si continutul raman ca si in edit

  const prevPostRef = useRef();
  useEffect(() => {
    prevPostRef.current = propsPost;
    console.log("PostForm useEffect. prevPost:", prevPostRef.current);
  }, [propsPost]);
  const prevPost = prevPostRef.current;
  //console.log("out in PostForm: prevPost:", prevPost);


  //const quillRef = useRef();
  useEffect(() => {
    if( prevPost && quillRef.current ) {
      if(propsPost.key !== prevPost.key) {
        console.log("PostForm. useEffect. Edit / Add switch");
        setTitle(propsPost.title);
        setContent(propsPost.content);
        //quillRef.current.setContents(``);
        quill.setContents("");
      }
    }
  }, [propsPost]);

  const handlePostForm = (event) => {
    event.preventDefault();
    //console.log("handlePostForm. propsPost = ", propsPost)
    if (title) {
      const newPost = {
        ...propsPost,
        title: title,
        content: content,
      };
      console.log("New post:", newPost);
      if(updatePost) {
        updatePost(newPost)
      } else {
        addNewPost(newPost);
      }
      setSaved(true);
    } else {
      alert("Title required")
    }
  };

  if(saved === true) {
    console.log("PostForm saved = true. Redirect to posts!")
    return <Navigate to="/" />
  }

  return (
    <form className="container" onSubmit={handlePostForm}>
      {addNewPost && <h1>Add New Post</h1>}
      {updatePost && <h1>Update Post: {params.postSlug}</h1>}
      {/*_ Title Fields Here _*/}
      <p>
        <label htmlFor="form-title">Title:</label>
        <br />
        <input
          id="form-title"
          value={title}
          onChange={ event => {
              setTitle(event.target.value);
              console.log("title onChange post=", title);
            }
          }
        />
      </p>

      {/*_ Quill Editor Here _*/}
      <p>
        <label htmlFor="form content">Content:</label>
      </p>

      <div style={{ height: 100, marginBottom: "55px" }}>
        <div ref={quillRef} />
      </div>

      <p>
        <button type="submit">Save</button>
      </p>
    </form>
  );
}

export default PostForm;
//<p style={{display: "block", height: 50, border: "2px solid red", margin: "100px"}}>
/*

*/
