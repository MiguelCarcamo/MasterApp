import React from 'react'
import { Grid, Paper, CardContent, Checkbox} from '@mui/material';
import Typography from '@mui/material/Typography';
import CountUp from 'react-countup';

function InformationBox(props) {

  return (
    <>
    <Grid item xs={12} md={4} lg={3}>
        <Paper sx={{ p: 2, display: 'flex', backgroundColor: props.color, flexDirection: 'column', height: '100%',}}>
            <CardContent>
                <Typography align='center' variant="h7">
                <Checkbox sx={{position: 'relative', top: 0, right: 0}} disabled checked={props.val}/>
                    {props.title} 
                </Typography>
                <Typography variant="h4" component="div">
                    <CountUp end={props.num2} />
                </Typography>
                <Typography variant="body2">
                    <br/>
                    New:<CountUp end={props.new} /> Update:<CountUp end={props.Update} />
                </Typography>
            </CardContent>
        </Paper>
    </Grid>
    </>
  )
}

export default InformationBox