// import React, { useEffect, useState } from 'react'
// import axios from 'axios';
// import { renderMatches, useNavigate } from 'react-router-dom';
// import { Form,FormField,TextInput,Box,Button,Header,Menu} from 'grommet';
 
// export const Login = () => {

//     useEffect(() => {
//         // Update the document title using the browser API
          
//       });
    
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [value, setValue] = useState({});
//     const [msg, setMsg] = useState('');
//     const navigate = useNavigate();
//     const [accessToken,setAccessToken] = useState('');
//     let axiosConfig = {
//         headers: {
//             'Content-Type': 'application/json;charset=UTF-8',
//             "Access-Control-Allow-Origin": "*",
//         }
//       };
//     const Auth = async (e) => {
//         e.preventDefault();
//         try {
//             await axios.post('login', {
//                 email_id: email,
//                 password: password,
//             },axiosConfig,).then((res) =>
//                 {
//                   console.log(res.data);
//                 });
//             navigate("/dashboard");
//         } catch (error) {
//             if (error.response) {
//                 setMsg(error.response.data.msg);
//                 alert('User is not registered');
//             }
//         }
//     }
    
           
//             return (
//               <Box>
//                 <Box>
//                   LOGIN FORM
//                 </Box>
              
//               <Form
//                 value={value}
//                 onChange={nextValue => setValue(nextValue)}
//                 onReset={() => setValue({})}
//                 onSubmit={Auth}
//               >
//                 <FormField name="email" htmlFor="text-input-id" label="Email-id" onChange={e => setEmail(e.target.value)}>
//                   <TextInput id="text-input-id" name="email-id" />
//                 </FormField>
//                 <FormField name="password" htmlFor="text-input-id" label="Password" onChange={e => setPassword(e.target.value)}>
//                   <TextInput id="text-input-id" name="password" />
//                 </FormField>
//                 <Box direction="row" gap="medium">
//                   <Button type="submit" primary label="Submit" />
//                   <Button type="reset" label="Reset" />
//                 </Box>
//               </Form>
//               </Box>
//             )
//           }
import React, { Component } from "react";
import { Link, useNavigate } from "react-router-dom";

class SignInForm extends Component {
  constructor() {
    super();

    this.state = {
      email: "",
      password: ""
    };

    this.handleChange = this.handleChange.bind(this);
    this.handleSubmit = this.handleSubmit.bind(this);
  }

  handleChange(event) {
    let target = event.target;
    let value = target.type === "checkbox" ? target.checked : target.value;
    let name = target.name;

    this.setState({
      [name]: value
    });
  }

  handleSubmit(event) {
    event.preventDefault();

    console.log("The form was submitted with the following data:");
    
    console.log(this.state);
    
  }

  render() {
    return (
      <div className="formCenter">
        <form className="formFields" onSubmit={this.handleSubmit}>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="email">
              E-Mail Address
            </label>
            <input
              type="email"
              id="email"
              className="formFieldInput"
              placeholder="Enter your email"
              name="email"
              value={this.state.email}
              onChange={this.handleChange}
            />
          </div>

          <div className="formField">
            <label className="formFieldLabel" htmlFor="password">
              Password
            </label>
            <input
              type="password"
              id="password"
              className="formFieldInput"
              placeholder="Enter your password"
              name="password"
              value={this.state.password}
              onChange={this.handleChange}
            />
          </div>

          <div className="formField">
            <button className="formFieldButton">Sign In</button>{" "}
            <Link to="/" className="formFieldLink">
              Create an account
            </Link>
          </div>
        </form>
      </div>
    );
  }
}

export default SignInForm;

        