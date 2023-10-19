import PostCard from './PostCard'

function MainFeed({posts}){

    return (
        <div>
             {posts.map(post => <PostCard />)}
        </div>
    )
}

export default MainFeed