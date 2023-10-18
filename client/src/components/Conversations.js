import {Link} from 'react-router-dom'

function Conversations({profile, logout, conversations}) {
    return (
        <div>
            <Link to = {`/${profile.username}/conversations`}>
            <h2>Welcome {profile.username}</h2>
            <button onClick = {logout}>Logout</button>
            {conversations?.map(conversation => (
                // <Link to = {`/${profile.username}/conversations`}>
                <h3 key = {conversation.id}>
                    {conversation.id} {conversation.message}
                </h3>
            ))}
            </Link>
        </div>
    )
}

export default Conversations