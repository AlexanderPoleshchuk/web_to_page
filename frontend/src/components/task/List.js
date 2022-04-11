import React, { Component, Fragment } from 'react';
import { connect } from 'react-redux';
import { PropTypes } from 'prop-types';
import { getTasks } from '../../actions/tasks';

class List extends Component {

    static propTypes = {
        tasks: PropTypes.array.isRequired,
        getTasks: PropTypes.func.isRequired,
    };

    componentDidMount() {
        this.props.getTasks();
    };

    render() {
        return (
            <Fragment>
                <h2>Web generator</h2>
                <table className='table table-striped'>
                    <thead>
                    <tr>
                        <th>Url</th>
                        <th>Email</th>
                        <th>status</th>
                        <th></th>
                    </tr>
                    </thead>
                    <tbody>
                    {this.props.tasks.map(task => (
                        <tr key={task.id}>
                            <td>{task.user_url}</td>
                            <td>{task.user}</td>
                            <td>{task.status}</td>
                        </tr>
                    ))}
                    </tbody>
                </table>
            </Fragment>
        )
    }
}


const mapStateToProps = (state) => ({
    tasks: state.tasks.tasks
});

export default connect(mapStateToProps, { getTasks })(List);