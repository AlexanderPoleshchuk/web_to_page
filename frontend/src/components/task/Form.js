import React, { Component } from 'react';
import { connect } from 'react-redux';
import PropTypes from 'prop-types';
import { addTasks } from '../../actions/tasks';

class Form extends Component {

    state = {
        user_url: '',
        user_email: ''
    };

    static propTypes = {
        addTasks: PropTypes.func.isRequired
    };

    onSubmit = (e) => {
        e.preventDefault();
        const { user_url, user_email } = this.state;
        const task = { user_url, user_email };
        this.props.addTasks(task);
        this.setState({
            user_url: '',
            user_email: ''
        });
    };

    onChange = (e) => this.setState({ [e.target.name]: e.target.value });

    render() {
        const { user_url, user_email } = this.state;

        return (
            <div className='card card-body mt-4 mb-4'>
                <h2>Generate</h2>
                <form onSubmit={this.onSubmit}>
                    <div className='form-group'>
                        <label>Url</label>
                        <input
                            type='url'
                            className='form-control'
                            name='user_url'
                            onChange={this.onChange}
                            value={user_url}
                            required
                        />

                    </div>
                    <div className='form-group'>
                        <label>Email</label>
                        <input
                            type='email'
                            className='form-control'
                            name='user_email'
                            onChange={this.onChange}
                            value={user_email}
                            required
                        />
                    </div>
                    <div className='form-group'>
                        <button type='submit' className='btn btn-primary'>Add</button>
                    </div>
                </form>
            </div>
        )
    }
}

export default connect(null, { addTasks })(Form);