import React, { useEffect, useState } from 'react'
import axios from 'axios';
import { renderMatches, useNavigate } from 'react-router-dom';
import { Form,FormField,TextInput,Box,Button} from 'grommet';
 
export const Login = () => {

    useEffect(() => {
        // Update the document title using the browser API
          
      });
    
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [value, setValue] = useState({});
    const [msg, setMsg] = useState('');
    const navigate = useNavigate();
    let axiosConfig = {
        headers: {
            'Content-Type': 'application/json;charset=UTF-8',
            "Access-Control-Allow-Origin": "*",
        }
      };
    const Auth = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:5000/login', {
                email: email,
                password: password,
            },axiosConfig);
            navigate("/dashboard");
        } catch (error) {
            if (error.response) {
                setMsg(error.response.data.msg);
                alert(msg);
            }
        }
    }
    
           
            return (
              <Form
                value={value}
                onChange={nextValue => setValue(nextValue)}
                onReset={() => setValue({})}
                onSubmit={Auth}
              >
                <FormField name="email" htmlFor="text-input-id" label="Email-id" onChange={e => setEmail(e.target.value)}>
                  <TextInput id="text-input-id" name="email-id" />
                </FormField>
                <FormField name="password" htmlFor="text-input-id" label="Password" onChange={e => setPassword(e.target.value)}>
                  <TextInput id="text-input-id" name="password" />
                </FormField>
                <Box direction="row" gap="medium">
                  <Button type="submit" primary label="Submit" />
                  <Button type="reset" label="Reset" />
                </Box>
              </Form>
            )
          }

        