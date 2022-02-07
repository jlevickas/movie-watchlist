import { HashRouter as Router, Routes, Route } from "react-router-dom";
import "./App.css";
import Header from "./components/Header";
import Footer from "./components/Footer";
import MovieList from "./pages/MovieList";

function App() {
  return (
    <Router>
      <div className="App">
        <Header />
        <Routes>
          <Route path="/" element={<MovieList />}></Route>
        </Routes>
        <Footer />
      </div>
    </Router>
  );
}

export default App;
