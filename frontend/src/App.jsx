import React from 'react'
import { BrowserRouter as Router, Route, Routes } from 'react-router-dom'
import Home from './components/Home'
import Login from './components/Login'
import Subscription from './components/Subscription'
import AboutPage from './components/AboutPage'
import Layout from './components/Layout'
import './App.css'

function App() {
  return (
    <>
      <Router>
        <Layout>
          <Routes>
            <Route path="/" element={<Home />} />
            <Route path="/login" element={<Login />} />
            <Route path="/about" element={<AboutPage />} />
            <Route path="/subscription" element={<Subscription />} />
          </Routes>
        </Layout>
      </Router>
    </>
  )
}

export default App
