import { initializeApp } from "firebase/app";
import { getAuth } from "firebase/auth";
import { getFirestore, collection, getDocs } from 'firebase/firestore/lite'
import { getDatabase } from "firebase/database";


//import "firebase/compat/database";

//console.log("fb", firebase.getApp);

const config = {
  apiKey: "AIzaSyAuZO8twbd0G5vHpARJlk9dTN0P_AXblKk",
  authDomain: "react-blog-demo-c0e02.firebaseapp.com",
  projectId: "react-blog-demo-c0e02",
  storageBucket: "react-blog-demo-c0e02.appspot.com",
  messagingSenderId: "837504335634",
  appId: "1:837504335634:web:a5b8eaaf6e050dc481fdcb"
};
const firebaseapp = initializeApp(config);
const firebaseauth = getAuth();

const firebasedb = getDatabase(firebaseapp);

console.log("firebasedb", firebasedb);

export { firebaseauth, firebasedb };
