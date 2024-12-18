import React from "react";
import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import { AuthProvider } from "./components/AuthContext";
import Home from "./components/Home";
import Login from "./components/Login";
import Register from "./components/Register";
import NewsList from "./components/NewsList";
import SummaryHome from "./components/summaryHome";
import SummarySubject from "./components/summarySubject";
import NewsTemplate from "./components/NewsTemplate";
import Subscription from "./components/Subscription";
import AboutPage from "./components/AboutPage";
import Layout from "./components/Layout";
import ResetPasswordPage from "./components/ResetPasswordPage";
import Profile from "./components/Profile"; // Profile 컴포넌트 import 추가
import Mail from "./components/Mail";
import "./App.css";

function App() {
  return (
    <AuthProvider>
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/reset-password" element={<ResetPasswordPage />} />
            <Route path="/ticker/:ticker" element={<NewsList />} />
            <Route path="/register" element={<Register />} />
            <Route path="/news" element={<NewsList />} />
            <Route path="/news/template" element={<NewsTemplate />} />
            <Route path="/articles/:id" element={<SummarySubject />} />
            <Route path="/summary" element={<SummaryHome />} />
            <Route path="/summary/:id" element={<SummarySubject />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/subscription" element={<Subscription />} />
            <Route path="/profile" element={<Profile />} />{" "}
            <Route path="/mail" element={<Mail />} />
          </Routes>
        </Layout>
      </Router>
    </AuthProvider>
  );
}

export default App;
