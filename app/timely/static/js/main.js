// get_user_id :: returns the in template/base.html injected user_id.
const get_user_id = () => {
    return JSON.parse(document.getElementById('user_id').textContent);
}

// get time from api
const get_time = async () => {
    let user_id = get_user_id();
    let response = await fetch(`http://localhost:8000/api/timer/${user_id}`)
    if (response.status === 200) {
        let data = await response.json();
        return data;
    } else {
        console.error(`An error occured\nStatus: ${response.status}`);
        return {'message': '00:00'}
    }
}
