// Import the functions you need from the SDKs you need
import { initializeApp } from "firebase/app";
import { getDatabase } from "firebase/database";
// TODO: Add SDKs for Firebase products that you want to use
// https://firebase.google.com/docs/web/setup#available-libraries

// Your web app's Firebase configuration
// For Firebase JS SDK v7.20.0 and later, measurementId is optional
const firebaseConfig = {
  apiKey: "AIzaSyBilFmMjrGI0TVhZ5h_gDvoO4PKzx-WDgs",
  authDomain: "door-robot.firebaseapp.com",
  projectId: "door-robot",
  storageBucket: "door-robot.appspot.com",
  messagingSenderId: "50752892487",
  appId: "1:50752892487:web:3f682cf4d7c1f34bc30b62",
  measurementId: "G-3BS3C5XBQV"
};

// Initialize Firebase
const firebase = initializeApp(firebaseConfig);
const db = getDatabase(firebase);

export default firebase;
export { db };
