import { BrowserRouter, Routes, Route} from 'react-router-dom'
import React from 'react';
import Menu from './Pages/Menu'
import NotFoundPage from './Pages/NotFoundPage'
import SignInSide from './Pages/SignInSide';


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route path="/" element={<SignInSide />} />
        <Route path="/Main" element={<Menu />} />
        <Route path="/Main/:ruta" element={<Menu />} />
        <Route path='*' element={<NotFoundPage />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;
