// import React, { useState } from 'react'
// import axios from "axios";
// import { useNavigate } from "react-router-dom";
// import { Form,FormField,TextInput,Box,Button} from 'grommet';
 
// export const Register = () => {
//     const [value,setValue] = useState({});
//     const [firstname, setFirstName] = useState('');
//     const [lastname, setLastName] = useState('');
//     const [email, setEmail] = useState('');
//     const [password, setPassword] = useState('');
//     const [confPassword, setConfPassword] = useState('');
//     const [msg, setMsg] = useState('');
//     const navigate = useNavigate();
 
//     const Register = async (e) => {
//         e.preventDefault();
//         try {
//             axios.post('/register', {
//                 // first_name: firstname,
//                 // last_name: lastname,
//                 email_id: email,
//                 password: password,
//                 //confPassword: confPassword
//             });
//             navigate("/");
//         } catch (error) {
//             if (error.response) {
//                 setMsg(error.response.data.msg);
//             }
//         }
//     }
    
//     return (
//       <Box>
//       <Box>
//         REGISTER FORM
//       </Box>
//         <Form
//                 value={value}
//                 onChange={nextValue => setValue(nextValue)}
//                 onReset={() => setValue({})}
//                 onSubmit={Register}
//               >
//                 {/* <FormField name="firstname" htmlFor="text-input-id" label="First Name" onChange={e => setFirstName(e.target.value)}>
//                   <TextInput id="text-input-id" name="firstname" />
//                 </FormField>
//                 <FormField name="lastname" htmlFor="text-input-id" label="Last Name" onChange={e => setLastName(e.target.value)}>
//                   <TextInput id="text-input-id" name="lastname" />
//                 </FormField> */}
//                 <FormField name="email" htmlFor="text-input-id" label="email" onChange={e => setEmail(e.target.value)}>
//                   <TextInput id="text-input-id" name="email" />
//                 </FormField>
//                 <FormField name="password" htmlFor="text-input-id" label="password" onChange={e => setPassword(e.target.value)}>
//                   <TextInput id="text-input-id" name="password" />
//                 {/* </FormField>
//                 <FormField name="confPassword" htmlFor="text-input-id" label="Confirm Password" onChange={e => setConfPassword(e.target.value)}>
//                   <TextInput id="text-input-id" name="confPassword" /> */}
//                 </FormField>
//                 <Box direction="row" gap="medium">
//                   <Button type="submit" primary label="Register" />
//                   <Button type="reset" label="Reset" />
//                 </Box>
//               </Form>
// </Box>
        
//     )

// }
 
// export default Register
import React, { Component } from "react";
import { Link } from "react-router-dom";
import axios from "axios";

class SignUpForm extends Component {
  constructor() {
    super();

    this.state = {
      email: "",
      password: "",
      firstname: "",
      lastname: "",
      hasAgreed: false
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

  handleSubmit(e) {
    e.preventDefault();

    console.log("The form was submitted with the following data:");
    console.log(this.state);
            try {
            axios.post('/register', {
                // first_name: firstname,
                // last_name: lastname,
                email_id: this.state.email,
                password: this.state.password,
                //confPassword: confPassword
            });
        } catch (error) {
            if (error.response) {
                console.log(error.response.data.msg);
            }
        }
    }
  

  render() {
    return (
      <div className="formCenter">
        <form onSubmit={this.handleSubmit} className="formFields">
          <div className="formField">
            <label className="formFieldLabel" htmlFor="name">
              First Name
            </label>
            <input
              type="text"
              id="firstname"
              className="formFieldInput"
              placeholder="Enter first name"
              name="firstname"
              value={this.state.firstname}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="name">
              Last Name
            </label>
            <input
              type="text"
              id="lastname"
              className="formFieldInput"
              placeholder="Enter last name"
              name="lastname"
              value={this.state.lastname}
              onChange={this.handleChange}
            />
          </div>
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
            <label className="formFieldLabel" htmlFor="password">
              Confirm Password
            </label>
            <input
              type="password"
              id="password"
              className="formFieldInput"
              placeholder="Re-enter your password"
              name="password"
              value={this.state.password}
              onChange={this.handleChange}
            />
          </div>

          

          <div className="formField">
            <button className="formFieldButton">Sign Up</button>{" "}
            <Link to="/sign-in" className="formFieldLink">
              I'm already member
            </Link>
          </div>
        </form>
      </div>
    );
  }
}
export default SignUpForm;