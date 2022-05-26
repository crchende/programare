import React from "react";

const Message = function({ type, info }) {
  const messages = {
    saved: "Post has been saved!",
    updated: "Post has been updated!",
    deleted: "Post has been deleted!",
    error: "Error while processing post. Check the console messages!",
    loginerror: "Login Error. ",
  }

  //console.log("type", type)
  //console.log("info", info)

  let msg = "";
  if(info === undefined) {
    msg = messages[type];
  } else {
    msg = messages[type] + info;
  }

  console.log(msg);

  return (
    <div className={`App-message $type`}>
      <p className="container">
        <strong>{msg}</strong>
      </p>
    </div>
  );
};

export default Message;
