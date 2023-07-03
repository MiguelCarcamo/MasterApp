import React, { useState, useEffect} from "react";
import { createTheme, ThemeProvider } from '@mui/material/styles';
import { NavLink, useParams  } from 'react-router-dom';

import CssBaseline from '@mui/material/CssBaseline';
import Box from '@mui/material/Box';
import Toolbar from '@mui/material/Toolbar';
import Container from '@mui/material/Container';
import Grid from '@mui/material/Grid';
import Paper from '@mui/material/Paper';
import AppBarNav from "../components/AppBar";
import Typography from '@mui/material/Typography';
import Breadcrumbs from '@mui/material/Breadcrumbs';

// componentes del body menu
import PromiseDate from "../components/PromiseDate";
import StyleBroad from "../components/StyleBroad";
import PowerBiPlanning from "../components/PowerBiPlanning";
import CustomerData from "../components/CustomerData";
import SupplyCycle from "../components/SupplyCycle";

import { IconButton } from '@mui/material';
import AutoModeIcon from '@mui/icons-material/AutoMode';
import Cookies from 'universal-cookie';
import { useMsal } from "@azure/msal-react";
import { useNavigate } from 'react-router-dom';

function Menu() {
  const [modo, setModo] = useState("light");
  const cookies = new Cookies();
  const navigate = useNavigate();
  const darkTheme = createTheme({
    palette: {
      // mode: 'light',
      mode: modo,
    },
  });
  const { ruta } = useParams();
  const { accounts } = useMsal();
    // EN ESTA SECCION CONTIENE TODAS LAS USEEFFECT QUE REQUERIMOS PARA EL FUNCIONAMIENTO
    useEffect(() => {
        // if (false) {
        if (accounts.length === 0) {
            cookies.remove('IDUser', {path: "/"});
            cookies.remove('UserName', {path: "/"});
            cookies.remove('UserLastName', {path: "/"});
            cookies.remove('UserMail', {path: "/"});
            navigate('/'); 
        }
    }, []);
  return (
    <ThemeProvider theme={darkTheme}>
      <Box sx={{ display: 'flex' }}>
        <CssBaseline />
        <AppBarNav />
        <Box
          component="main"
          sx={{
            backgroundColor: (theme) =>
              theme.palette.mode === 'light'
                ? theme.palette.grey[100]
                : theme.palette.grey[900],
            flexGrow: 1,
            height: '100vh',
            overflow: 'auto',
          }}
        >
          <Toolbar />
          <Container maxWidth="xl" sx={{ mt: 4, mb: 4 }}>
            <Grid container spacing={3}>
              {/* Recent Orders */}
              <Grid maxWidth="100%" item xs={12}>
                <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                <Breadcrumbs aria-label="breadcrumb">
                  
                  <Typography color="text.primary">
                    <NavLink to={'/Main/'}>
                      Main
                    </NavLink>
                  </Typography>
                  <Typography color="text.primary">{ruta}</Typography>
                  <IconButton onClick={() => modo === 'light'? setModo("dark"):setModo("light")} color="primary" component="label">
                    <AutoModeIcon />
                  </IconButton>
                </Breadcrumbs>
                </Paper>
                {(ruta) ?
                <Paper sx={{ p: 2, display: 'flex', flexDirection: 'column' }}>
                  {
                    {
                      'PromisedDate': <PromiseDate />,
                      'StyleBroad': <StyleBroad />,
                      'CAPlanning': <PowerBiPlanning />,
                      'CustomerData': <CustomerData />,
                      'SupplyCycle': <SupplyCycle />,
                    }[ruta]
                  }
                  
                </Paper>
                : null
                }
                
              </Grid>
            </Grid>
          </Container>
        </Box>
      </Box>
    </ThemeProvider>
  )
}

export default Menu