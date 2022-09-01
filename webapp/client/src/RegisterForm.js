import React from 'react';
import {useState} from 'react';

import {Form,FormField,Box,Header,Footer} from 'grommet';

const Registerform = () =>  {

    const [errorMessages, setErrorMessages] = useState({});
    const [isSubmitted, setIsSubmitted] = useState(false);

    const renderErrorMessage = (name) =>
    name === errorMessages.name && (
    <div className="error">{errorMessages.message}</div>
  );

  const handleSubmit = (event) => {
    event.preventDefault();
  };


  return (
    <Box>
        <Header>
            Register Form
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
      </Form>
    </Box>
    </Box>
 );
}

export default Registerform;