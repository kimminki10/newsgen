import React from 'react';
import Header from './Header';
import './Layout.css';

const Layout = ({ children }) => {
    return (
        <div className="layout">
            <Header />
            <main className="main-content">
                {children}
            </main>
            <footer className="footer">모든 투자에 대한 책임은 투자자 본인에게 있습니다</footer>
        </div>
    );
};

export default Layout;