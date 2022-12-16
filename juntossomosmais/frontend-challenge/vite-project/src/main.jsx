import React from 'react'
import ReactDOM from 'react-dom/client'

import App from './App'
import GlobalStyles from './styles/GlobalStyles'
import Header from './components/header'

ReactDOM.createRoot(document.getElementById('root')).render(
  <React.StrictMode>
    <GlobalStyles />
    <Header />
    <App />
  </React.StrictMode>,
)
