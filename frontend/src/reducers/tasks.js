import { GET_TASK_LIST, ADD_TASK} from '../actions/types';

const initialState = {
    tasks: []
};

// eslint-disable-next-line import/no-anonymous-default-export
export default function (state = initialState, action) {
    switch (action.type) {
        case GET_TASK_LIST:
            return {
                ...state,
                tasks: action.payload
            };
        case ADD_TASK:
            return {
                ...state,
                tasks: [...state.tasks, action.payload]
            };
        default:
            return state;
    }
};