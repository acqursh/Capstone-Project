import React from 'react';
import {Routes,Route} from 'react-router-dom';
import Loginform from './loginform';
import Registerform from './RegisterForm';


function PageRoutes(){
    return (
        <Routes>
            <Route path="/" element={<Loginform/>}/>
            <Route path="/register" element={<Registerform/>}/>
        </Routes>
    )
};

export default PageRoutes;