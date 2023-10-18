import {Link} from 'react-router-dom'

function Conversations({profile, logout, conversations}) {
    return (
        <div>
             <h2>Welcome {profile.username}</h2>
                <button onClick = {logout}>Logout
                <Link to = '/'></Link>
                </button>
                {conversations.map(conversation => (
                    <h3 key = {conversation.id}>
                        <Link to = {`/${profile.username}/conversations`}>  {profile.conversations} </Link>
                    {conversation.message} 
                    </h3>
                ))}
        </div>
    )
}

export default Conversations