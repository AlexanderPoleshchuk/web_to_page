import axios from 'axios';
import { GET_TASK_LIST, ADD_TASK } from './types';

// axios.defaults.xsrfHeaderName = 'X-CSRFTOKEN';
// axios.defaults.xsrfCookieName = 'csrftoken';

export const getTasks = () => dispatch => {
    axios.get('http://0.0.0.0:8000/api/web_generator/')
        .then(result => {
            dispatch({
                type: GET_TASK_LIST,
                payload: result.data
            });
        }).catch(error => console.log(error));
};

export const addTasks = (task) => dispatch => {
    axios.post('http://0.0.0.0:8000/api/web_generator/', task)
        .then(result => {
            dispatch({
                type: ADD_TASK,
                payload: result.data
            });
        }).catch(error => console.log(error));
};