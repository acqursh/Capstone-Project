// import { BrowserRouter, Route, Routes } from "react-router-dom";
// import {Dashboard} from "./components/Dashboard";
// import {Login} from "./components/Login";
// import {Navbar} from "./components/Navbar";
// import {Register} from "./components/Register";
// import {SampleRegister} from "./components/SampleRegister"
// import "./App.css";

// function App() {
//   return (
//     <BrowserRouter>
//       <Routes>
//         <Route path="/" element={<Login />} />
//         <Route path="/register" element={<Register/>} />
//         <Route path="/dashboard" element={<Dashboard/>} />
//       </Routes>
//     </BrowserRouter>
//   );
// }
 
// export default App;
import React, { Component } from "react";
import { HashRouter as Router, Route, NavLink,Routes } from "react-router-dom";
import SignUpForm from "./components/Register";
import SignInForm from "./components/Login"; 
import Dashboard from "./components/Dashboard"; 

import "./App.css";

class App extends Component {
  render() {
    return (
      <Router basename="/">
        <div className="App">
          <div className="appAside" />
          <div className="appForm">
            <div className="pageSwitcher">
              <NavLink
                to="/sign-in"
                activeClassName="pageSwitcherItem-active"
                className="pageSwitcherItem"
              >
                Sign In
              </NavLink>
              <NavLink
                exact
                to="/"
                activeClassName="pageSwitcherItem-active"
                className="pageSwitcherItem"
              >
                Sign Up
              </NavLink>
              <NavLink
                exact
                to="/home"
                activeClassName="pageSwitcherItem-active"
                className="pageSwitcherItem"
              >
                Home
              </NavLink>
            </div>

            {/* <div className="formTitle">
              <NavLink
                to="/sign-in"
                activeClassName="formTitleLink-active"
                className="formTitleLink"
              >
                Sign In
              </NavLink>{" "}
              or{" "}
              <NavLink
                exact
                to="/"
                activeClassName="formTitleLink-active"
                className="formTitleLink"
              >
                Sign Up
              </NavLink>
            </div> */}
            <Routes>
            <Route exact path="/" element={<SignUpForm/>} />
            <Route path="/sign-in" element={<SignInForm/>} />
            <Route path="/home" element={<Dashboard/>} />
            </Routes>
            
          </div>
        </div>
      </Router>
    );
  }
}

export default App;