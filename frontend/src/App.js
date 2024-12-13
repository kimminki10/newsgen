import './App.css';
import TopHeader from './components/TopHeader';

function App() {
  return (
    <div className="App">
      <TopHeader />
      <header className="App-header">
        <h1>NewsGen</h1>
        <div className="auth-buttons">
          <button>Login</button>
          <button>Sign Up</button>
        </div>
      </header>
    </div>
  );
}

export default App;