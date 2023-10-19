import {Link} from 'react-router-dom'


function PostCard({profile, posts}) {
    return (
        <div>
            {/* <Link to = {`/${profile.username}/posts/${post.id}`}> */}
                {posts.map(post => (
                    <Link to = {`/${profile.username}/posts/${post.id}`}>
                    <h1>{post.title}</h1>
                    <p>{post.content}</p>
                    </Link>
                ))}
            {/* </Link> */}
        </div>
)}





export default PostCard