import React from 'react';
import Header from "./components/layout/Header";
import DashBoard from "./components/task/Dashboard";


function App() {
  return (
      <div className='container'>
          <Header />
          <DashBoard />
      </div>
  );
}

export default App;
