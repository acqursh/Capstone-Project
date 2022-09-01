import React from 'react';
import {useState} from 'react';
import { useNavigate } from 'react-router-dom';

import {Form,FormField,Box,Header,Footer,Button} from 'grommet';

const Loginform = () =>  {

    let navigate = useNavigate();
    const [errorMessages, setErrorMessages] = useState({});
    const [isSubmitted, setIsSubmitted] = useState(false);

    const renderErrorMessage = (name) =>
    name === errorMessages.name && (
    <div className="error">{errorMessages.message}</div>
  );

  const handleSubmit = (event) => {
    event.preventDefault();
  };

  const handleRegister = () => {
    navigate('/register')
  }

  return (
    <Box>
        <Header>
            Login Form
        </Header>
    <Box>
      <Form onSubmit={handleSubmit}>
        <div className="input-container">
          <label>Username </label>
          <input type="text" name="uname" required />
          {renderErrorMessage("uname")}
        </div>
        <div className="input-container">
          <label>Password </label>
          <input type="password" name="pass" required />
          {renderErrorMessage("pass")}
        </div>
        <div className="button-container">
          <input type="submit" />
        </div>
        <Box>
            <Button label='click to register' primary onClick={handleRegister}/>
        </Box>
      </Form>
    </Box>
    </Box>
 );
}

export default Loginform;