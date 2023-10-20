import {Link} from 'react-router-dom'

function UserPosts({profile, logout, posts}) {

    return (
        <div className='setScreen text-center bg-gray-300'>
             <h2 className='font-bold text-5xl  bg-green-500 text-pink-400' >Welcome {profile.username}</h2>
                <div className='grid grid-cols-2 gap-y-6 text-3xl mt-6 underline'>
                    {posts.map((post) => (
                        <Link to = {`/${profile.username}/posts/${post.id}`}>
                            <h3 key={post.id}>
                                {post.title}
                            </h3>
                        </Link>
                    ))}
                </div>
                <button onClick = {logout} className='underline font-bold'>Logout
                    <Link to = '/'></Link>
                </button>
        </div>
    )
}

export default UserPosts

