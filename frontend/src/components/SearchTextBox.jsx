import React from "react";
import { FontAwesomeIcon } from "@fortawesome/react-fontawesome";
import { faSearch } from "@fortawesome/free-solid-svg-icons";
import './SearchTextBox.css';

const SearchTextBox = ({ type, placeholder, value, onChange }) => {
    return (
        <div className='search-text-box'>
            <input 
                className="search-input"
                type={type} 
                placeholder={placeholder} 
                value={value} 
                onChange={onChange} 
            />
            <button className="search-button">
                <FontAwesomeIcon icon={faSearch} />
            </button>
        </div>
    );
}

export default SearchTextBox;