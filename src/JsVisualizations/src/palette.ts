import Color from 'color';

const blue = '#003f5c';
const pink = '#bc5090';

export default {
    blue,
    blueTransparent: Color(blue).alpha(0.2).hsl().string(),
    purple: '#58508d',
    pink,
    pinkTransparent: Color(pink).alpha(0.2).hsl().string(),
    red: '#ff6361',
    yellow: '#ffa600'
};