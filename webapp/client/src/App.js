import Loginform from './loginform';
import RegisterForm from './RegisterForm';
import './App.css';
import { createContext, useReducer, useState } from 'react';
import PageRoutes from './Routes';
import {BrowserRouter as Router} from "react-router-dom";

export const UserContext = createContext();

function App() {

  const [user,setUser] = useState({
    first_name: "",
    last_name: "",
    email: "",
  });

  return (
    <Router>
      <PageRoutes/>
    </Router>
  );
}

export default App;
