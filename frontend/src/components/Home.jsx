import React from 'react'
import Header from './Header'
import NewsList from './NewsList';
import './Home.css'

const Home = () => {
    return (
        <div className="home">
            <Header />
            <h1>Welcome to the Home Page</h1>
            <div className='content'>
                <div className='subscription-section'>
                    <NewsList />
                </div>
                <div className='all-section'>
                    <NewsList />
                </div>
            </div>
        </div>
    )
};

export default Home;