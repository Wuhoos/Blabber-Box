import {NavLink} from "react-router-dom";

function NavBar ({ profile })  {
    console.log(profile)
    return (
        <nav className="navbar text-center text-2xl bg-black text-white">
            <NavLink className="links mr-8 hover:bg-purple-600 font-sans hover:font-serif" to="/posts">Main Feed</NavLink>
            <NavLink className="links hover:bg-purple-600 font-sans hover:font-serif" to={`/${profile?.username}/posts`}>My Posts</NavLink>
        </nav>
    )
}

export default NavBar;