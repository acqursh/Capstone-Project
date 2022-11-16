/* eslint-disable react-hooks/exhaustive-deps */
import React, { useState, useEffect } from 'react'
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
    const [show,setShow] = useState(true);
    return (
        <Box>
            <Box>
                <Navbar/>
            </Box>
            {/* <Box>
                <Button label="ADD USER DATA" type='submit' onClick={setShow(true)} />
            </Box> */}
            {show && (
            <Box>
            <UserDataForm accessToken={accessToken} />
            </Box>
            
            )}
            <Box>
                <ECGform accessToken={accessToken}/>
            </Box>
            
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
  );
}
const UserDataForm = (props) => {
    
    const [cp, setcp] = React.useState();
    const [trtbps, settrtbps] = React.useState();
    const [chol, setchol] = React.useState();
    const [fbs, setfbs] = React.useState();
    const [slp, setslp] = React.useState();
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
        const response = await axios.post("user_attr", {
            'cp': cp,
            'trtbps': trtbps,
            'chol': chol,
            'fbs': fbs,
            'slp': slp,
        }, axiosConfig)
        console.log(response);
        }
        catch(error){
            console.log(error);
        }
    }
  return (
    <Form
      value={value}
      onReset={() => setValue({})}
      onSubmit={onSubmit}
    >
      <FormField name="cp" htmlFor="text-input-id" label="Chest Pain" onChange={e => setcp(e.target.value)}>
        <input type="number" id="cp" name="name" />
      </FormField>
      <FormField name="trtbps" htmlFor="text-input-id" label="Blood Pressure" onChange={e => settrtbps(e.target.value)}>
        <input type="number" id="trtbps" name="name" />
      </FormField>
      <FormField name="chol" htmlFor="text-input-id" label="Cholestrol" onChange={e => setchol(e.target.value)}>
        <input type="number" id="chol" name="name" />
      </FormField>
      <FormField name="fbs" htmlFor="text-input-id" label="Fasting Blood Pressure" onChange={e => setfbs(e.target.value)}>
        <input tyep="number" id="fbs" name="name" />
      </FormField>
      <FormField name="slp" htmlFor="text-input-id" label="Slope" onChange={e => setslp(e.target.value)}>
        <input type="number" id="slp" name="name" />
      </FormField>
      <Box direction="row" gap="medium">
        <Button type="submit" primary label="Submit" />
        <Button type="reset" label="Reset" />
      </Box>
    </Form>
  );
}
export default Dashboard