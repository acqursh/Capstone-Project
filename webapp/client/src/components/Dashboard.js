/* eslint-disable react-hooks/exhaustive-deps */
import React, { useState, useEffect, Component } from 'react'
import axios from 'axios';
import jwt_decode from "jwt-decode";
import { useNavigate } from 'react-router-dom';
import Navbar from './Navbar';
import {Card,CardBody,CardHeader,CardFooter,Button,Box,Layer,Form,FormField,TextInput} from "grommet";

 
export const Dashboard = () => {
    const [name, setName] = useState('');
    const [token, setToken] = useState('');
    const [expire, setExpire] = useState('');
    const [users, setUsers] = useState([]);
    const [accessToken,setAccessToken] = useState('');
    const navigate = useNavigate();
    
    useEffect(() => {
        fitbitToken();
        registerFitbit();
        //refreshToken();
        //getUsers();
        
        // axios.get('fitbit_register',axiosConfig).then((res) =>
        //     {
        //       console.log(res.data);
        //     });
    }, []);
 
    
    const registerFitbit = async () => {
        let axiosConfig = {
            headers: {
                'Content-Type': 'application/json;charset=UTF-8',
                "Access-Control-Allow-Origin": "*",
                "Authorization": `Bearer ${accessToken}`,
            }
          };
        try {
            const response = await axios.get("fitbit_register",axiosConfig);
            //setAccessToken(response.data.accessToken);
            console.log(response);
        } catch (error) {
            console.log(error);
        }
    }
    const fitbitToken = async () => {
        try {
            const response = await axios.post("login",{
                email_id: "arko.pal2000@gmail.com",
                password: "12345"
            });
            //setAccessToken(response.data.accessToken);
            console.log(response.data.access_token);
            setAccessToken(response.data.access_token);
        } catch (error) {
            console.log(error);
        }
        }
    
    const refreshToken = async () => {
        try {
            const response = await axios.get('http://localhost:5000/token');
            // console.log('hello');
            // console.log(response);
            setToken(response.data.accessToken);
            const decoded = jwt_decode(response.data.accessToken);
            setName(decoded.name);
            setExpire(decoded.exp);
        } catch (error) {
            if (error.response) {
                navigate("/");
            }
        }
    }
 
    const axiosJWT = axios.create();
 
    axiosJWT.interceptors.request.use(async (config) => {
        const currentDate = new Date();
        if (expire * 1000 < currentDate.getTime()) {
            const response = await axios.get('http://localhost:5000/token');
            config.headers.Authorization = `Bearer ${response.data.accessToken}`;
            setToken(response.data.accessToken);
            const decoded = jwt_decode(response.data.accessToken);
            setName(decoded.name);
            setExpire(decoded.exp);
        }
        return config;
    }, (error) => {
        return Promise.reject(error);
    });
 
    // const getUsers = async () => {
    //     const response = await axiosJWT.get('http://localhost:5000/users', {
    //         headers: {
    //             Authorization: `Bearer ${token}`
    //         }
    //     });
    //     setUsers(response.data);
    //}
    const handleUpdateEcg = async() => {
      setUpdateVitals(false);
      setShowVitals(false);
      setUpdateEcg(true);
    }
    const handleUpdateVitals = async() => {
      setUpdateVitals(true);
      setShowVitals(false);
      setUpdateEcg(false);
        
    }
    const handleDisplayVitals = async() => {
      setShowVitals(true);
      setUpdateEcg(false);
      setUpdateVitals(false);
    }

    const [showVitals,setShowVitals] = useState(true);
    const [updateVitals,setUpdateVitals] = useState(false);
    const [showEcg,setUpdateEcg] = useState(false);
    return (
        <Box>
          <Box direction='row' gap='medium'>
          <Box>
            <Button label="Display Vitals" onClick={handleDisplayVitals}></Button>
          </Box>
          <Box>
            <Button label='Update Vitals' onClick={handleUpdateVitals}></Button>
          </Box>
          <Box>
            <Button label='Update ECG' onClick={handleUpdateEcg}></Button>
          </Box>
          </Box>
            {updateVitals && (
            <Box>
            <UserDataForm accessToken={accessToken} />
            </Box>
            
            )}
            {showEcg && (
            <Box>
                <ECGform accessToken={accessToken}/>
            </Box>
            )}
            {showVitals && (
            <Box>
              <UserDetails accessToken={accessToken}/>
            </Box>
            )}
        </Box>
        
    )
}
const ECGform = (props) => {
    let accessToken = props.accessToken;
    let axiosConfig = {
        headers: {
            'Content-Type': 'multipart/form-data',
            "Access-Control-Allow-Origin": "*",
            "Authorization": `Bearer ${accessToken}`,
        }
      };
      const [files,setFile] = useState(null);
      const [value,setValue] = useState({});
      const onSubmit = async() => {
        try{
            var formData = new FormData();
            formData.append('file',files[0]);

            const response = await axios.patch("ecg",formData,axiosConfig);
            console.log(response);
        }
        catch(error){
            console.log(error);
        }
      }

      return (  
      <Box>
        <Box>
          <br/>
        </Box>
        <Box>
          
      <Form
      value={value}
      onReset={() => setValue({})}
      onSubmit={onSubmit}
    >
      <FormField name="ecg" htmlFor="text-input-id" label="ECG REPORT" onChange={e => setFile(e.target.files)}>
        <input type="file" id="ecg" name="ecg" />
      </FormField>
      <Box direction="row" gap="medium">
        <Button type="submit" primary label="Submit" />
        <Button type="reset" label="Reset" />
      </Box>
    </Form>
    </Box>
    </Box>
  );
}
// const UserDataForm = (props) => {
    
    // const [cp, setcp] = React.useState();
    // const [trtbps, settrtbps] = React.useState();
    // const [chol, setchol] = React.useState();
    // const [fbs, setfbs] = React.useState();
    // const [slp, setslp] = React.useState();
    // const [value,setValue] = useState({});
    //  let accessToken = props.accessToken;
    
    // let axiosConfig = {
    //     headers: {
    //         'Content-Type': 'application/json;charset=UTF-8',
    //         "Access-Control-Allow-Origin": "*",
    //         "Authorization": `Bearer ${accessToken}`,
    //     }
    //   };
    
    
    //   const onSubmit = async() => {
    //     try{
    //     const response = await axios.post("user_attr", {
    //         'cp': cp,
    //         'trtbps': trtbps,
    //         'chol': chol,
    //         'fbs': fbs,
    //         'slp': slp,
    //     }, axiosConfig)
    //     console.log(response);
    //     }
    //     catch(error){
    //         console.log(error);
    //     }
    // }
    //
    class UserDataForm extends Component {
    constructor() {
      super();
  
      this.state = {
        email: "",
        password: "",
        name: "",
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
    }
  //
  render(){
  return (
    // <Form
    //   value={value}
    //   onReset={() => setValue({})}
    //   onSubmit={onSubmit}
    // >
    //   <FormField name="cp" htmlFor="text-input-id" label="Chest Pain" onChange={e => setcp(e.target.value)}>
    //     <input type="number" id="cp" name="name" />
    //   </FormField>
    //   <FormField name="trtbps" htmlFor="text-input-id" label="Blood Pressure" onChange={e => settrtbps(e.target.value)}>
    //     <input type="number" id="trtbps" name="name" />
    //   </FormField>
    //   <FormField name="chol" htmlFor="text-input-id" label="Cholestrol" onChange={e => setchol(e.target.value)}>
    //     <input type="number" id="chol" name="name" />
    //   </FormField>
    //   <FormField name="fbs" htmlFor="text-input-id" label="Fasting Blood Pressure" onChange={e => setfbs(e.target.value)}>
    //     <input tyep="number" id="fbs" name="name" />
    //   </FormField>
    //   <FormField name="slp" htmlFor="text-input-id" label="Slope" onChange={e => setslp(e.target.value)}>
    //     <input type="number" id="slp" name="name" />
    //   </FormField>
    //   <Box direction="row" gap="medium">
    //     <Button type="submit" primary label="Submit" />
    //     <Button type="reset" label="Reset" />
    //   </Box>
    // </Form>
    <div className="formCenter">
        <form onSubmit={this.handleSubmit} className="formFields">
          <div>
            <br/>
          </div>

          <div className="formField">
            <label className="formFieldLabel" htmlFor="name">
              CP
            </label>
            <input
              type="text"
              id="name"
              className="formFieldInput"
              placeholder="Enter chest pain type"
              name="name"
              value={this.state.name}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="name">
              TRTBPS
            </label>
            <input
              type="text"
              id="name"
              className="formFieldInput"
              placeholder="Enter trtbps"
              name="name"
              value={this.state.name}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="name">
              CHOL
            </label>
            <input
              type="text"
              id="name"
              className="formFieldInput"
              placeholder="Enter cholestrol"
              name="name"
              value={this.state.name}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="name">
              FBS
            </label>
            <input
              type="text"
              id="name"
              className="formFieldInput"
              placeholder="Enter fasting blood sugar"
              name="name"
              value={this.state.name}
              onChange={this.handleChange}
            />
          </div>
          <div className="formField">
            <label className="formFieldLabel" htmlFor="name">
              SLP
            </label>
            <input
              type="text"
              id="name"
              className="formFieldInput"
              placeholder="Enter SLP"
              name="name"
              value={this.state.name}
              onChange={this.handleChange}
            />
          </div>
          <div>
          <Box direction="row" gap="medium">
            <Button type="submit" primary label="Submit" />
            <Button type="reset" label="Reset" />
         </Box>
         </div>
          
          </form>
          </div>
  );
  }
}


function UserDetails(props){
  const [value,setValue] = useState({});
  let accessToken = props.accessToken;
  let axiosConfig = {
    headers: {
        'Content-Type': 'application/json;charset=UTF-8',
        "Access-Control-Allow-Origin": "*",
        "Authorization": `Bearer ${accessToken}`,
    }
  };
  const onSubmit = async() => {
    try{
      const response = await axios.get("users",axiosConfig)
      console.log(response);
      }
      catch(error){
          console.log(error);
      }
      setMessage(true);
  }
  const [message,setMessage] = useState();
  return (
    <Box>
      <Box>
        <br/>
        <br/>
        <br/>
      </Box>
      <Box>
      <table>
        <tr>
          <td>Age</td>
          <td>21</td>
        </tr>
        <tr>
          <td>Sex</td>
          <td>Male</td>
        </tr>
        <tr>
          <td>Maximum Heart Rate recorded</td>
          <td>73</td>
        </tr>
        <tr>
          <td>Chets Pain Type</td>
          <td>Typical Angina</td>
        </tr>
        <tr>
          <td>Fasting Blood Sugar</td>
          <td>90</td>
        </tr>
        <tr>
          <td>Blood Cholestrol</td>
          <td>140</td>
        </tr>
        <tr>
          <td>Blood Pressure</td>
          <td>145</td>
        </tr>
        <tr>
          <td>Resting ECG category</td>
          <td>Normal</td>
        </tr>
        <tr>
          <td>Slope</td>
          <td>1</td>
        </tr>
      </table>
      </Box>
      <Box>
        <br/>
        <br/>
        <br/>
      </Box>
      <Box gap="medium">
        <Button type="submit" primary label="Generate Report" onClick={onSubmit} />
      </Box>
      <br/>
      
      {message && (
            <Box>
              The report has been sent to your registered email id.
            </Box>
            )}

    </Box>
  );
}
export default Dashboard