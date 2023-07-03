import React, { useState, useEffect } from 'react';
import { Container, Paper, Box, TextField, Grid, Button, ButtonGroup, Dialog, Typography,  Autocomplete} from '@mui/material';
import AddIcon from '@mui/icons-material/Add';
import LinearProgress from '@mui/material/LinearProgress';
import SendIcon from '@mui/icons-material/Send';
import InformationBox from './InformationBox';
import Stack from '@mui/material/Stack';
import Alert from '@mui/material/Alert';
import swal from 'sweetalert';
import axios from 'axios';

//Librerias para exportar a excel
import * as FileSaver from 'file-saver';
import XLSX from 'sheetjs-style';

function SupplyCycle() {
    // Variables
    const URL = 'https://arnpythondev.tegraglobal.com:5000/api/';
    const [file, setFile] = useState(false);
    const [LineFile, setLineFile] = useState(true);
    const [open, setOpen] = useState(false);
    const [open2, setOpen2] = useState(false);
    const [open3, setOpen3] = useState(false);
    const [CycleData, setCycleData] = useState([]);
    const [forecastData, setforecastData] = useState(false);
    const [CustomerData, setCustomerData] = useState([]);
    const [PlantData, setPlantData] = useState([]);
    const [VarCylce, setVarCylce] = useState(null);
    const [formCycle , setFormCycle] = useState({
        id : 0,
        Name : "",
        StartDate : "",
        EndDate : "",
        Comments : ""
    })
    const [formForecast , setFormForecast] = useState({
        id : 0,
        Id_Style_Customer : null,
        Id_Demand_Cycle : null,
        CustomerForecastDate : "",
        Status : 1,
        Comments : ""
    })
    const [formOnPO , setFormOnPO] = useState({
        id : 0,
        IDPlant : null,
        Id_Demand_Cycle : null,
        LastDateBuy : "",
        Status : 1,
        Comments : ""
    })

    // Funciones
    const handleChange = (e) => {
        const {id , value} = e.target   
        setFormCycle(prevState => ({
            ...prevState,
            [id] : value
            })
        )
    }
    const handleChange2 = (e) => {
        const {id , value} = e.target   
        setFormForecast(prevState => ({
            ...prevState,
            [id] : value
            })
        )
    }
    const handleChange3 = (e) => {
        const {id , value} = e.target   
        setFormOnPO(prevState => ({
            ...prevState,
            [id] : value
            })
        )
    }
    const EnviarDatos1 = async () => {
        try{
            var url = URL + 'Demand_Cycle/add/1'
            const data = await fetch(url, {
              method: 'POST',
              headers: {'Content-Type':'application/json'},
              body: JSON.stringify(formCycle)
              }
            );
            setFormCycle({Name : "", StartDate:"", EndDate:"", Comments : ""});
            swal({
                title: 'Shortlisted!',
                text: 'Data Updated successfully!',
                icon: 'success'
              });
            setOpen(false);
            UpdateData1();
        } catch (error) {
            console.log(error); 
        }
    }
    const EnviarDatos2 = async () => {
        const form = new FormData();
        form.append('File', file);
        for (const key in formForecast) {
            if (key == 'Id_Style_Customer' || key == 'Id_Demand_Cycle'){
                form.append(key, formForecast[key].split('-')[0]);
            }else{
                form.append(key, formForecast[key]);
            }
        }
        let url = 'https://arnpythondev.tegraglobal.com:5000/api/FileForecast/NIKE/2023';
        try{
            const x = await axios({
                method: "post",
                url: url,
                data: form,
                headers: { "Content-Type": "multipart/form-data" },
              });
              if(x.data.length > 0){
                setforecastData(x.data);
              }
        }catch(err) {

        }
    }
    const UpdateData1 = async () =>  {
        try {
            var url = URL + 'Demand_Cycle/'
            const data = await fetch(url);
            const data1 = await data.json();
            setCycleData(data1);
        } catch (error) {
           console.log(error); 
        }
    }
    const UpdateData2 = async () =>  {
        try {
            var url = URL + 'Style_Customer/'
            const data = await fetch(url);
            const data1 = await data.json();
            setCustomerData(data1);
        } catch (error) {
           console.log(error); 
        }
    }
    const UpdateData3 = async () =>  {
        try {
            var url = URL + 'Plant/'
            const data = await fetch(url);
            const data1 = await data.json();
            setPlantData(data1);
        } catch (error) {
           console.log(error); 
        }
    }

    const fileType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8";
    const fileExtension = ".xlsx";
    const exportToExcel = async (Data,name) =>{
        const ws = XLSX.utils.json_to_sheet(Data);
        const wb = { Sheets: { 'data': ws}, SheetNames: ['data']};
        const excelBuffer = XLSX.write(wb, { bookType:'xlsx', type: 'array'});
        const data = new Blob([excelBuffer], {type: fileType});
        FileSaver.saveAs(data, name + fileExtension);
    }

    useEffect(() => {
        UpdateData1();
        UpdateData2();
        UpdateData3();
    }, []);
    useEffect(() => {
        const enviarDatosAsync = async () => {
            try {
                if (file) {
                    setLineFile(false);
                    await EnviarDatos2();
                    setLineFile(true);
                }
            } catch (error) {
                console.error('Error al enviar datos:', error);
            }
        };
    
        enviarDatosAsync();
    }, [file]);
  return (
        <div style={{ height: 625, width: '100%' }}>
            <ButtonGroup variant="outlined" aria-label="outlined primary button group">
                <Button onClick={() => setOpen(true)} variant="outlined" color="success" startIcon={<AddIcon />} >Cycle</Button>
                <Button onClick={() => setOpen2(true)} variant="outlined" color="success" startIcon={<AddIcon />} >Forecast</Button>
                <Button onClick={() => setOpen3(true)} variant="outlined" color="success" startIcon={<AddIcon />} >OnPO</Button>
                
            </ButtonGroup>
            <Autocomplete style={{ width: '25%' }}
                    id="free-solo-demo"
                    onChange={(event, newValue) => {
                        setVarCylce(newValue);
                    }}
                    value={VarCylce}
                    options={(CycleData)?CycleData.map((option) =>option.id + '-' + option.Name):[]}
                    renderInput={(params) => <TextField {...params} label="Cycle" />}
                />
            <Container maxWidth="lg" sx={{ mt: 4, mb: 4 }}>
                <Grid container spacing={3}>
                    <InformationBox color='#80cbd9' title='Forecast' />
                    <InformationBox color='#83cf80' title='OnPO' />
                    <InformationBox color='#77c6e0' title='Forecast Placeholder' />
                    <InformationBox color='#e0da84' title='Styles Pending' />
                </Grid>
            </Container>
            <Dialog open={open} onClose={() => setOpen(false)} fullWidth maxWidth="sm" >
                <Grid component={Paper} elevation={6} square>
                    <Box sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column', alignItems: 'center',}}>
                        <Typography component="h1" variant="h5">Cycle's</Typography>
                            <TextField onChange={handleChange} value={formCycle.Name} margin="normal" fullWidth id="Name" label="Name" name="Name"/>
                            <TextField onChange={handleChange} InputLabelProps={{shrink: true,}} value={formCycle.StartDate} type="date" margin="normal" fullWidth id="StartDate" label="StartDate" name="StartDate"/>
                            <TextField onChange={handleChange} InputLabelProps={{shrink: true,}} value={formCycle.EndDate} type="date" margin="normal" fullWidth id="EndDate" label="EndDate" name="EndDate"/>
                            <TextField onChange={handleChange} value={formCycle.Comments} margin="normal" fullWidth id="Comments" label="Comments" name="Comments"/>
                        <Button onClick={EnviarDatos1} fullWidth variant="contained" color="success" endIcon={<SendIcon />}>
                            save
                        </Button>
                    </Box>
                </Grid>
            </Dialog>
            <Dialog open={open2} onClose={() => setOpen2(false)} fullWidth maxWidth="sm" >
                <Grid component={Paper} elevation={6} square>
                    <Box sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column', alignItems: 'center',}}>
                        <Typography component="h1" variant="h5">Forecast</Typography>
                            <Autocomplete
                                fullWidth
                                id="Id_Demand_Cycle"
                                onChange={(event, newValue) => {
                                    setFormForecast(prevState => ({
                                        ...prevState,
                                        ["Id_Demand_Cycle"] : newValue
                                        })
                                    )
                                }}
                                value={formForecast.Id_Demand_Cycle}
                                options={(CycleData)?CycleData.map((option) =>option.id + '-' + option.Name):[]}
                                renderInput={(params) => <TextField {...params} label="Cycle" />}
                            />
                            <br/>
                            <Autocomplete
                                fullWidth
                                id="Id_Style_Customer"
                                onChange={(event, newValue) => {
                                    setFormForecast(prevState => ({
                                        ...prevState,
                                        ["Id_Style_Customer"] : newValue
                                        })
                                    )
                                }}
                                value={formForecast.Id_Style_Customer}
                                options={(CustomerData)?CustomerData.map((option) =>option.id + '-' + option.Style_Customer):[]}
                                renderInput={(params) => <TextField {...params} label="Customer" />}
                            />
                            <TextField onChange={handleChange2} InputLabelProps={{shrink: true,}} value={formForecast.CustomerForecastDate} type="date" margin="normal" fullWidth id="CustomerForecastDate" label="CustomerForecastDate" name="CustomerForecastDate"/>
                            <TextField onChange={handleChange2} value={formForecast.Comments} margin="normal" fullWidth id="Comments" label="Comments" name="Comments"/>
                            <Box hidden={LineFile} sx={{ width: '100%' }}>
                                <LinearProgress />
                            </Box>
                            <TextField type="File" onChange={(e) => setFile(e.target.files[0]) } fullWidth />
                            {forecastData?
                            // {true?
                            <Stack sx={{ width: '100%' }} spacing={2}>
                                <Alert severity="info">
                                    {forecastData.length.toLocaleString()} rows loaded!!
                                </Alert>
                                <ButtonGroup>
                                    <Button variant="contained" style={{ backgroundColor: '#279989' }}>Save Data</Button>
                                    <Button variant="contained" onClick={(e) => exportToExcel(forecastData,'Forecast')} style={{ backgroundColor: '#658D1B' }}>Excel Data </Button>  
                                </ButtonGroup>
                            </Stack>
                            :false}
                    </Box>
                </Grid>
            </Dialog>
            <Dialog open={open3} onClose={() => setOpen3(false)} fullWidth maxWidth="sm" >
                <Grid component={Paper} elevation={6} square>
                    <Box sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column', alignItems: 'center',}}>
                        <Typography component="h1" variant="h5">Forecast</Typography>
                            <Autocomplete
                                fullWidth
                                id="Id_Demand_Cycle"
                                onChange={(event, newValue) => {
                                    setFormOnPO(prevState => ({
                                        ...prevState,
                                        ["Id_Demand_Cycle"] : newValue
                                        })
                                    )
                                }}
                                value={formOnPO.Id_Demand_Cycle}
                                options={(CycleData)?CycleData.map((option) =>option.id + '-' + option.Name):[]}
                                renderInput={(params) => <TextField {...params} label="Cycle" />}
                            />
                            <br/>
                            <Autocomplete
                                fullWidth
                                id="IDPlant"
                                onChange={(event, newValue) => {
                                    setFormOnPO(prevState => ({
                                        ...prevState,
                                        ["IDPlant"] : newValue
                                        })
                                    )
                                }}
                                value={formOnPO.Id_Style_Customer}
                                options={(PlantData)?PlantData.map((option) =>option.id + '-' + option.Plant):[]}
                                renderInput={(params) => <TextField {...params} label="Plant" />}
                            />
                            <TextField onChange={handleChange3} InputLabelProps={{shrink: true,}} value={formOnPO.LastDateBuy} type="date" margin="normal" fullWidth id="LastDateBuy" label="LastDateBuy" name="LastDateBuy"/>
                            <TextField onChange={handleChange3} value={formOnPO.Comments} margin="normal" fullWidth id="Comments" label="Comments" name="Comments"/>
                            <TextField type="File" onChange={(e) => setFile(e.target.files[0]) } fullWidth />
                            <br/>
                        <Button onClick={EnviarDatos2} fullWidth variant="contained" color="success" endIcon={<SendIcon />}>
                            ViewFile
                        </Button>
                    </Box>
                </Grid>
            </Dialog>
        </div>
  )
}

export default SupplyCycle