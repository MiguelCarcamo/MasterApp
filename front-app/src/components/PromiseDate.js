import React, { useState, useEffect } from 'react';
import Container from '@mui/material/Container';
import Paper from '@mui/material/Paper';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import TextField from '@mui/material/TextField';
import Autocomplete from '@mui/material/Autocomplete';
import { Button, ButtonGroup} from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import Box from '@mui/material/Box';
import LinearProgress from '@mui/material/LinearProgress';
import axios from 'axios';
//Librerias para exportar a excel
import * as FileSaver from 'file-saver';
import XLSX from 'sheetjs-style';
import Alert from '@mui/material/Alert';
import Collapse from '@mui/material/Collapse';
import CloseIcon from '@mui/icons-material/Close';
import IconButton from '@mui/material/IconButton';
import swal from 'sweetalert';

const columns = [
    { field: 'Po_Number', headerName: 'PO Weekly', width: 180 },
    { field: 'PO Number', headerName: 'PO PPM', width: 180 },
    { field: 'MO', headerName: 'MO PPM', width: 150 },
    { field: 'Cut', headerName: 'Cut·', width: 60 },
    { field: 'PromisedDate', headerName: 'Promised Date', width: 150 },
    { field: 'PromisedDateProcess', headerName: 'Promised Date Process', width: 180 },
    { field: 'Status', headerName: 'Status', width: 150 },
    { field: 'QuantityOrdered', headerName: 'Qty', width: 80 },
    { field: 'Comments', headerName: 'Comments', width: 200 },
  ];
  
  
function PromiseDate() {
    const [BtnLook, setBtnLook] = useState(true);
    const [rows, setRows] = useState(false);
    const [rowsSave, setRowsSave] = useState(false);
    const [rowsNA, setRowsNA] = useState(false);
    const [DataPlant, setDataPlant] = useState(false);
    const [Plant, setPlant] = useState(null);
    const [Process, setProcess] = useState(null);
    const [LineProcess, setLineProcess] = useState(true);
    const [file, setFile] = useState(null);
    const [CantPO, setCantPO] = useState(0);
    const [CantPONA, setCantPONA] = useState(0);
    const [PDEmpty, setPDEmpty] = useState(0);
    const [PDPEmpty, setPDPEmpty] = useState(0);
    const [open, setOpen] = useState(false);
    const DataProcess = [
        { label: 'Sewing', id: 1 },
        { label: 'Cutting', id: 2 },
        { label: 'Embroidery', id: 3 },
        { label: 'EmbroideryFG', id: 4 },
        { label: 'ScreePrintingCP', id: 5 },
        { label: 'ScreePrintingFG', id: 14 },
        { label: 'Sublimated', id: 6 },
        { label: 'Plotter', id: 7 },
        { label: 'Carrusel', id: 8 },
        { label: 'CarruselFG', id: 15 },
        { label: 'Perforation', id: 9 },
        { label: 'Twill', id: 10 },
        { label: 'Nameplate', id: 11 },
        { label: 'PadPrint', id: 12 },
        { label: 'HeatTransfer', id: 13 },
      ];
    let url1 = "https://arnpythondev.tegraglobal.com:5000/api/Plant/";
    const UpdateData = async () =>  {
        try {
            const data = await axios(url1);
            const data1 = await data.data;
            setDataPlant(data1);
        } catch (error) {
           console.log(error); 
        }
    }
    let url2 = "https://arnpythondev.tegraglobal.com:5000/api/File/add";
    const UploadFile = async () =>  {
        setOpen(false);
        setLineProcess(false);
        const form = new FormData();
        form.append('File', file);
        form.append('Process', Process);
        form.append('Plant', Plant.split('-')[1]);
        console.log(form);
        try{
            const x = await axios({
                method: "post",
                url: url2,
                data: form,
                headers: { "Content-Type": "multipart/form-data" },
              });
            if(x.data.length > 0){
                setRows(x.data);
                setCantPO(x.data.length);
                setCantPONA(x.data.filter(i=> i.Status === 'NULL').length);
                setPDEmpty(x.data.filter(i=> i.PromisedDate === 'NULL').length);
                setPDPEmpty(x.data.filter(i=> i.PromisedDateProcess === 'NULL').length);
                setRowsNA(x.data.filter(i=> i.Status === 'NULL'));
                setRowsSave(x.data.filter(i=> i.PromisedDateProcess !== 'NULL' && i.Status !== 'NULL'))
                setLineProcess(true);
            }else{
                setLineProcess(true);
                setOpen(true);
            }
        }catch(err) {
            setLineProcess(true);
            setOpen(true);
        }
    }
    const SaveData =  async () =>  {
        setLineProcess(false);
        let datax = JSON.stringify(rowsSave);
        let url3 = "https://arnpythondev.tegraglobal.com:5000/api/PromisedDate/add/"+Plant.split('-')[0]+"/"+Process;
        let customConfig = {
            headers: {
            'Content-Type': 'application/json'
            }
        };
        await axios.post(url3, datax, customConfig);
        swal("Good job!", "You clicked the button!", "success");
        setLineProcess(true);
    }
    useEffect(() => {
        const run = async () =>
            await UpdateData();
        run();
    }, []);
    useEffect(() => {
        if((file != null && Process != null && Plant != null)){
            setBtnLook(false);
        }else{
            setBtnLook(true);
        }
    }, [file, Process, Plant]);

    const fileType = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet;charset=UTF-8";
    const fileExtension = ".xlsx";
    const exportToExcel = async (Data,name) =>{
        const ws = XLSX.utils.json_to_sheet(Data);
        const wb = { Sheets: { 'data': ws}, SheetNames: ['data']};
        const excelBuffer = XLSX.write(wb, { bookType:'xlsx', type: 'array'});
        const data = new Blob([excelBuffer], {type: fileType});
        FileSaver.saveAs(data, name + fileExtension);
    }

  return (
    <>
        <Container component="main" maxWidth="md" sx={{ mb: 4 }}>
            <Paper variant="outlined" sx={{ my: { xs: 4, md: 7 }, p: { xs: 3, md: 4 } }}>
            <Box hidden={LineProcess} sx={{ width: '100%' }}>
                <LinearProgress />
            </Box>
            <Typography component="h1" variant="h4" align="center">
                Promised Date
            </Typography>
            <Grid container spacing={3}>
                <Grid item xs={12} sm={6}>
                    <Autocomplete
                        onChange={(event, newValue) => {
                            setPlant(newValue);
                        }}
                        value={Plant}
                        options={(DataPlant)?DataPlant.map((option) =>option.id + '-' + option.Plant):[]}
                        renderInput={(params) => <TextField {...params} label="Plant" />}
                    />
                </Grid>
                <Grid item xs={12} sm={6}>
                    <Autocomplete
                        onChange={(event, newValue) => {
                            setProcess(newValue);
                        }}
                        value={Process}
                        options={(DataProcess)?DataProcess.map((option) =>option.label):[]}
                        renderInput={(params) => <TextField {...params} label="Process" />}
                    />
                </Grid>
                <Grid item xs={12}>
                    <TextField type="File" onChange={(e) => setFile(e.target.files[0])} fullWidth></TextField>
                </Grid>
                <Grid item xs={12} sm={6}>
                <ButtonGroup variant="contained">
                    <Button disabled={BtnLook} onClick={UploadFile} variant="contained" style={{ backgroundColor: '#00A9EO' }}>Upload File</Button>
                </ButtonGroup>
                </Grid>
            </Grid>
            <Collapse in={open}>
                <Alert
                severity="error"
                action={
                    <IconButton
                    aria-label="close"
                    color="inherit"
                    size="small"
                    onClick={() => {
                        setOpen(false);
                    }}
                    >
                    <CloseIcon fontSize="inherit" />
                    </IconButton>
                }
                sx={{ mb: 2 }}
                >
                Error al consultar los datos de PPM(Verifique el Formato y vuélvalo a intentar.) :D
                </Alert>
            </Collapse>
            </Paper>
        </Container>
        {rows?
        <div style={{ height: '100%', width: '100%' }}>
            <ButtonGroup variant="contained" aria-label="outlined primary button group">
                <Button variant="contained" onClick={SaveData} style={{ backgroundColor: '#279989' }}>Save Data</Button>
                <Button variant="contained" onClick={(e) => exportToExcel(rowsNA,'PromisedDate')} style={{ backgroundColor: '#658D1B' }}>Excel Data </Button>
            </ButtonGroup>
            <Box sx={{ height: 400, width: '100%' }}>
                <Typography align="center">
                    Cantidad de PO: {CantPO}, Not found: {CantPONA}, PromisedDate Vacias: {PDEmpty}, PromisedDateProcess Vacias: {PDPEmpty} [PO Correctas: {rowsSave.length}]
                </Typography>
                    <DataGrid sx={{ height: '100%', width: '100%' }}
                        rows={rows}
                        columns={columns}
                    />
            </Box>
        </div>
        : false}
    </>
  )
}
export default PromiseDate