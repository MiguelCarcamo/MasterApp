import React, { useEffect } from 'react';
import Avatar from '@mui/material/Avatar';
import CssBaseline from '@mui/material/CssBaseline';
import Paper from '@mui/material/Paper';
import Box from '@mui/material/Box';
import Grid from '@mui/material/Grid';
import LockOutlinedIcon from '@mui/icons-material/LockOutlined';
import Typography from '@mui/material/Typography';
import { createTheme, ThemeProvider } from '@mui/material/styles';
import img from './img/test.jpg'
import img2 from './img/test2.jpg'
import Button from '@mui/material/Button';
import AdminPanelSettingsIcon from '@mui/icons-material/AdminPanelSettings';
import { useMsal } from "@azure/msal-react";
import { useNavigate } from 'react-router-dom';
import Cookies from 'universal-cookie';

const theme = createTheme();
const cookies = new Cookies();

export default function SignInSide() {
    const navigate = useNavigate();
    const { instance, accounts, inProgress } = useMsal();
    const iniciarSesion = async ()=> {
        try {
            await instance.loginPopup();
            // cookies.set('IDUser', "TEST", {path: "/"});
            // cookies.set('UserName', "TEST", {path: "/"});
            // cookies.set('UserLastName', "TEST", {path: "/"});
            // cookies.set('UserMail', "TEST", {path: "/"});
            // navigate('/Main'); 
        } catch (error) {
           console.log(error); 
        }
    }
    // EN ESTA SECCION CONTIENE TODAS LAS USEEFFECT QUE REQUERIMOS PARA EL FUNCIONAMIENTO
    useEffect(() => {
        if (accounts.length > 0) {
            cookies.set('IDUser', accounts[0].localAccountId, {path: "/"});
            cookies.set('UserName', accounts[0].name.split(' ')[0], {path: "/"});
            cookies.set('UserLastName', accounts[0].name.split(' ')[1], {path: "/"});
            cookies.set('UserMail', accounts[0].username, {path: "/"});
            navigate('/Main'); 
        }
    }, [instance, inProgress]);
    return (
    <ThemeProvider theme={theme}>
        <Grid container component="main" sx={{ height: '100vh' }}>
            <CssBaseline />
        <Grid
          item
          xs={false}
          sm={4}
          md={9}
          sx={{
            backgroundImage: `url(${img})`,
            backgroundRepeat: 'no-repeat',
            backgroundColor: (t) =>
              t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
            backgroundSize: 'cover',
            backgroundPosition: 'center',
          }}
        />
        <Grid backgroundColor="#D9D9D6" item xs={12} sm={8} md={3} component={Paper} elevation={6} square 
            sx={{
                backgroundImage: `url(${img2})`,
                backgroundRepeat: 'no-repeat',
                backgroundColor: (t) =>
                t.palette.mode === 'light' ? t.palette.grey[50] : t.palette.grey[900],
                backgroundSize: 'cover',
                backgroundPosition: 'center',
            }}  
        >
            <Box
                sx={{
                my: 8,
                mx: 4, 
                display: 'flex',
                flexDirection: 'column',
                alignItems: 'center',
                }}
            >
                <Avatar sx={{ width: 80, height: 80, m: 1, bgcolor: 'black' }}>
                    <LockOutlinedIcon sx={{ fontSize: 50 }} />
                </Avatar>
                <Typography component="h1" variant="h5">Supply Planning App</Typography>
                <Typography component="h2" variant="h6">Version: Beta 1.x</Typography>
                <Box component="form" noValidate sx={{ mt: 1 }}>
                    <Button onClick={iniciarSesion} endIcon={<AdminPanelSettingsIcon />} fullWidth variant="contained" sx={{ mt: 3, mb: 2 }} >
                        Sign In
                    </Button>
                    
                </Box>
            </Box>
        </Grid>
        </Grid>
    </ThemeProvider>
  );
}