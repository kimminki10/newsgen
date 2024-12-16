import React, { useState } from "react";
import { useNavigate } from "react-router-dom";
import "./Register.css";

const TextBox = ({ label, type, placeholder, value, onChange }) => {
  return (
    <div className="text-box">
      <label>{label}</label>
      <input
        type={type}
        placeholder={placeholder}
        value={value}
        onChange={onChange}
      />
    </div>
  );
};

const Register = () => {
  const navigate = useNavigate();
  const [formData, setFormData] = useState({
    email: "",
    password: "",
    confirmPassword: "",
    name: "",
    phone: "",
  });

  const handleChange = (field) => (e) => {
    setFormData({
      ...formData,
      [field]: e.target.value,
    });
  };

  const handleSubmit = (e) => {
    e.preventDefault();
    // 회원가입 로직 구현
    console.log("Registration data:", formData);
  };

  const handleBackToLogin = () => {
    navigate("/login");
  };

  return (
    <div className="register-container">
      <h1>Register</h1>
      <form onSubmit={handleSubmit}>
        <TextBox
          label="Email"
          type="email"
          placeholder="Enter email"
          value={formData.email}
          onChange={handleChange("email")}
        />
        <TextBox
          label="Password"
          type="password"
          placeholder="Enter password"
          value={formData.password}
          onChange={handleChange("password")}
        />
        <TextBox
          label="Confirm Password"
          type="password"
          placeholder="Confirm password"
          value={formData.confirmPassword}
          onChange={handleChange("confirmPassword")}
        />
        <TextBox
          label="Name"
          type="text"
          placeholder="Enter your name"
          value={formData.name}
          onChange={handleChange("name")}
        />
        <TextBox
          label="Phone"
          type="tel"
          placeholder="Enter phone number"
          value={formData.phone}
          onChange={handleChange("phone")}
        />
        <button type="submit" className="registerBtn">
          Register
        </button>
        <div className="button-container">
          <button type="button" onClick={handleBackToLogin}>
            Back to Login
          </button>
        </div>
      </form>
    </div>
  );
};

export default Register;
