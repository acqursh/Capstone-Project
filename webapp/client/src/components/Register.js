import React, { useState } from 'react'
import axios from "axios";
import { useNavigate } from "react-router-dom";
import { Form,FormField,TextInput,Box,Button} from 'grommet';
 
export const Register = () => {
    const [value,setValue] = useState({});
    const [firstname, setFirstName] = useState('');
    const [lastname, setLastName] = useState('');
    const [email, setEmail] = useState('');
    const [password, setPassword] = useState('');
    const [confPassword, setConfPassword] = useState('');
    const [msg, setMsg] = useState('');
    const navigate = useNavigate();
 
    const Register = async (e) => {
        e.preventDefault();
        try {
            axios.post('/register', {
                // first_name: firstname,
                // last_name: lastname,
                email_id: email,
                password: password,
                //confPassword: confPassword
            });
            navigate("/");
        } catch (error) {
            if (error.response) {
                setMsg(error.response.data.msg);
            }
        }
    }
 
    return (
      <Box>
      <Box>
        REGISTER FORM
      </Box>
        <Form
                value={value}
                onChange={nextValue => setValue(nextValue)}
                onReset={() => setValue({})}
                onSubmit={Register}
              >
                {/* <FormField name="firstname" htmlFor="text-input-id" label="First Name" onChange={e => setFirstName(e.target.value)}>
                  <TextInput id="text-input-id" name="firstname" />
                </FormField>
                <FormField name="lastname" htmlFor="text-input-id" label="Last Name" onChange={e => setLastName(e.target.value)}>
                  <TextInput id="text-input-id" name="lastname" />
                </FormField> */}
                <FormField name="email" htmlFor="text-input-id" label="email" onChange={e => setEmail(e.target.value)}>
                  <TextInput id="text-input-id" name="email" />
                </FormField>
                <FormField name="password" htmlFor="text-input-id" label="password" onChange={e => setPassword(e.target.value)}>
                  <TextInput id="text-input-id" name="password" />
                {/* </FormField>
                <FormField name="confPassword" htmlFor="text-input-id" label="Confirm Password" onChange={e => setConfPassword(e.target.value)}>
                  <TextInput id="text-input-id" name="confPassword" /> */}
                </FormField>
                <Box direction="row" gap="medium">
                  <Button type="submit" primary label="Register" />
                  <Button type="reset" label="Reset" />
                </Box>
              </Form>
</Box>
        
    )
}
 
export default Register