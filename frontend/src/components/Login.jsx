import React from 'react';
import './Login.css';

const TextBox = ({ label, type, placeholder, value, onChange }) => {
    return (
        <div className='text-box'>
            <label>{label}</label>
            <input type={type} placeholder={placeholder} value={value} onChange={onChange} />
        </div>
    );
}

const Login = () => {
    return (
        <div className='login-container'>
            <h1>Login</h1>
            <TextBox label="Email" type="email" placeholder="Enter email" />
            <TextBox label="Password" type="password" placeholder="Enter password" />

            <button className='loginBtn'>Login</button>
            <div className='button-container'>
                <button>Find your account</button>
                <button>register</button>
            </div>
        </div>
    );
};

export default Login;