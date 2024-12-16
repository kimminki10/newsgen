import React from "react";


const SearchTextBox = ({ label, type, placeholder, value, onChange }) => {
    return (
        <div className='search-text-box'>
            <input type={type} placeholder={placeholder} value={value} onChange={onChange} />
            <button>Search</button>
        </div>
    );
}

export default SearchTextBox;