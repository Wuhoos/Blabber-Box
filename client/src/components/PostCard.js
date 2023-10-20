import { useParams } from 'react-router-dom'
import { useEffect, useState } from 'react'

function PostCard({ profile }) {
    const [displayedPost, setDisplayedPost] = useState({})
    const params = useParams()  

    useEffect(() => {
        fetch(`/${profile?.username}/posts/${params.id}`)
            .then(response => {
                if (response.ok) {
                    response.json()
                        .then(data => setDisplayedPost(data))
                }
                else {
                    setDisplayedPost({})
                }
            })
    }, [profile])

    function deletePost(id) {
        fetch (`/${profile.username}/post/` + id, {
            method: 'DELETE'
        })
        .then (response => {
            if(response.ok) {
                setDisplayedPost({})
            }else{
                console.log(response)
            }
        })  
    }


    return (
        <div className='setScreen  bg-gray-300 text-center'>
            <h1 className='text-6xl font-bold bg-green-500'>{displayedPost.title}</h1>
            <p className='mt-8 border-4 mx-7 border-pink-300'>{displayedPost.content}</p>
            {profile?.id === displayedPost.profile_id && <button onClick = {() => deletePost(params.id)}> Delete Post </button>}
            
        </div>
    )
}





export default PostCard