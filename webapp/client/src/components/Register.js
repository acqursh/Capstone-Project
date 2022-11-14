import React, { useState } from 'react'
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Form,FormField,TextInput,Box,Button} from 'grommet';
 
export const Register = () => {
    const [value,setValue] = useState({});
    const [name, setName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confPassword, setConfPassword] = useState('');
    const [msg, setMsg] = useState('');
    const navigate = useNavigate();
 
    const Register = async (e) => {
        e.preventDefault();
        try {
            await axios.post('http://localhost:5000/users', {
                name: name,
                email: email,
                password: password,
                confPassword: confPassword
            });
            navigate("/");
        } catch (error) {
            if (error.response) {
                setMsg(error.response.data.msg);
            }
        }
    }
 
    return (
        <Form
                value={value}
                onChange={nextValue => setValue(nextValue)}
                onReset={() => setValue({})}
                onSubmit={Register}
              >
                <FormField name="name" htmlFor="text-input-id" label="Name" onChange={e => setName(e.target.value)}>
                  <TextInput id="text-input-id" name="name" />
                </FormField>
                <FormField name="email" htmlFor="text-input-id" label="email" onChange={e => setEmail(e.target.value)}>
                  <TextInput id="text-input-id" name="email" />
                </FormField>
                <FormField name="password" htmlFor="text-input-id" label="password" onChange={e => setPassword(e.target.value)}>
                  <TextInput id="text-input-id" name="password" />
                </FormField>
                <FormField name="confPassword" htmlFor="text-input-id" label="Confirm Password" onChange={e => setConfPassword(e.target.value)}>
                  <TextInput id="text-input-id" name="confPassword" />
                </FormField>
                <Box direction="row" gap="medium">
                  <Button type="submit" primary label="Register" />
                  <Button type="reset" label="Reset" />
                </Box>
              </Form>

        
    )
}
 
export default Register