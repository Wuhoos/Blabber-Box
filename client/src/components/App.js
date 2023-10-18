import React, { useEffect, useState } from "react";
import { Switch, Route, useHistory } from "react-router-dom";
import Home from './Home'
import Conversations from './Conversations'


function App() {
  const [profile, setProfile] = useState(null)
  const [conversations, setConversations] = useState([])
  let history = useHistory()

  useEffect(() => {
    fetch('/check_login')
    .then(response => {
      if (response.ok) {
        response.json()
        .then(data => setProfile(data))
      }
    })
  }, [])

  useEffect(() => {
      profile &&
      fetch(`/${profile.username}/conversations`)
      .then(response => {
        if (response.ok) {
          
          response.json()
          .then(data => {setConversations(data)})
        } else{
          setConversations([])
        }
      })
    
    
  }, [profile])

  function attemptLogin(profileInfo) {
    fetch('/login', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json',
      },
      body: JSON.stringify(profileInfo)
    })
      .then((res)=>res.json())
      .then((data) => {
        setProfile(data)
        history.push(`/${data.username}/conversations`)
      });
  }

  function attemptSignup(profileInfo) {
    fetch('/profile', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'Accepts': 'application/json',
      },
      body: JSON.stringify(profileInfo),
    })
    .then((res)=>res.json())
    .then((data) => {
      setProfile(data)
      history.push(`/${data.username}/conversations`)
    })
  }

  function logout() {
    fetch('/logout', {
      method: 'DELETE'
    })
    .then(res => {if (res.ok) {    
      setProfile(null)
      history.push('/')
    }})
  }


  return (
    <div>
      <Switch>
        <Route path = '/:username/conversations'>
          {profile ? (<Conversations profile = {profile} logout = {logout} conversations = {conversations} />) : null}
        </Route>
        <Route exact path = '/'>
          <Home attemptLogin = {attemptLogin} attemptSignup = {attemptSignup} profile = {profile} />
        </Route>
      </Switch>
    </div>
  )
}

export default App;
