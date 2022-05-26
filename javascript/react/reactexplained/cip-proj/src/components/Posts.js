import React, { useContext } from "react";
import { Link } from "react-router-dom";
import UserContext from "../context/UserContext";

const Posts = ( {posts, deletePost} ) => {
  console.log("Posts: posts =", posts, ", length = ", posts.length);
  console.log(typeof(posts))

  const { user } = useContext(UserContext);

  //p1 = posts.map(post => {})
  // La map am => ( si nu => { pentru ca vreau sa fortez un return.
  // daca pun => { trebuie sa am explicit return

  return(<article className="posts container">
    <h1>Posts</h1>
    <ul>
      {posts.length < 1 && (<li key="empty">No posts yet!</li>)}
      { posts.map(post => (
        <li key={post.id}>
          <h2><Link stye={{disply: "inline", marginBottom: "10px"}} to={`post/${post.slug}`}>{post.title}</Link></h2>
          {user.isAuthenticated && (
              <p>
                <Link to={`/edit/${post.slug}`}>Edit</Link>
                {" | "}
                <button className="linkLike" onClick={() => deletePost(post)}>Delete</button>
              </p>
          )}
        </li>
      ))}
    </ul>
  </article>
  )
};

export default Posts;

/*

{ posts.map(post => (
  <li key={post.id}>
    <h2><Link stye={{disply: "inline", marginBottom: "10px"}} to={`post/${post.slug}`}>{post.title}</Link></h2>
    <Link to={`/edit/${post.slug}`}>Edit</Link>
    {" | "}
    <button className="linkLike" onClick={() => deletePost(post)}>Delete</button>
  </li>
))}

*/
