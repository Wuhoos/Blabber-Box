import {Link} from 'react-router-dom'

function Posts({profile, logout, posts}) {

    return (
        <div>
             <h2>Welcome {profile.username}</h2>
                <button onClick = {logout}>Logout
                <Link to = '/'></Link>
                </button>
                {posts.map((post) => (
                    <Link to = {`/${profile.username}/posts/${post.id}`}>
                        <h3 key={post.id}>
                            {post.title}
                        </h3>
                    </Link>
                ))}
        </div>
    )
}

export default Posts

