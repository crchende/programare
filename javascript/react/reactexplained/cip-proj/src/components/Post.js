import React from "react";
import { useParams } from "react-router-dom"

import { QuillDeltaToHtmlConverter } from "quill-delta-to-html";

import NotFound from "./NotFound";

const Post = ( props ) => {
  const params = useParams();
  console.log("Post params: ", params);

  //daca nu destructuram props cu { posts }, se poate accesa posts ca parte a obiectului props
  //console.log("props.posts: ", props.posts);
  //const post = props.posts.find(p => p.id === Number(params.postSlug)); //url param is named slug in any case
  //                                                                       if id used as slug, should be converted to integer

  const post = props.posts.find(p => p.slug === params.postSlug);

  var contentHTML = "";

  console.log("post: ", post);
  if(post.content.ops) {
    const converter = new QuillDeltaToHtmlConverter(post.content.ops, {});
    contentHTML = converter.convert();
  } else {
    contentHTML = post.content;
  }

  if(post) {
    return(
      <article className="post container">
        <h1>{post.title}</h1>
        <div
          className="content"
          dangerouslySetInnerHTML={{
              __html: contentHTML
          }}
        />
      </article>
    );
  } else {
    return <NotFound />
  }
}

export default Post;
