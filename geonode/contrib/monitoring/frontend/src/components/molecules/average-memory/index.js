import React from 'react';
import PropTypes from 'prop-types';
import HoverPaper from '../../atoms/hover-paper';
import styles from './styles';


class AverageMemory extends React.Component {
  static propTypes = {
    memory: PropTypes.number.isRequired,
  }

  render() {
    return (
      <HoverPaper style={styles.content}>
        <h5>Average Memory</h5>
        <div style={styles.stat}>
          <h3>{this.props.memory}%</h3>
        </div>
      </HoverPaper>
    );
  }
}


export default AverageMemory;