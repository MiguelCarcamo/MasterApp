import React, { useState, useEffect } from 'react';
import { Paper, Box, TextField, Grid, Button, ButtonGroup, Dialog, Typography,  Autocomplete} from '@mui/material';
import { DataGrid } from '@mui/x-data-grid';
import AddIcon from '@mui/icons-material/Add';
import RefreshIcon from '@mui/icons-material/Refresh';
import SendIcon from '@mui/icons-material/Send';
import swal from 'sweetalert';

function CustomerData() {
    const URL = 'https://arnpythondev.tegraglobal.com:5000/api/';
    const [rowDataEdi, setRowDataEdi] = useState([]);
    const [open, setOpen] = useState(false);
    const [open2, setOpen2] = useState(false);
    const [open3, setOpen3] = useState(false);
    const [DataProductType, setDataProductType] = useState([]);
    const [DataVendor, setDataVendor] = useState([]);
    const [ProductType, setProductType] = useState("");
    const [IDProductType, setIDProductType] = useState(null);
    const [Comments, setComments] = useState("");
    const [Vendor, setVendor] = useState("");
    const [IDVendor, setIDVendor] = useState(null);
    const [StyleNumber, setStyleNumber] = useState("");
    const [Colorway, setColorway] = useState("");
    const [Procurement, setProcurement] = useState("");
    const [Mfg, setMfg] = useState("");
    const [GIPT, setGIPT] = useState("");
    const [CommentsVendor, setCommentsVendor] = useState("");    
    const [rowData, setRowData] = useState();
    const [columns, setColumns] = useState([
        { field: 'id', headerName: 'ID', width: 100 },
        { field: 'StyleName', headerName: 'StyleName', width: 200 },
        { field: 'Style_ProductType', headerName: 'ProductType', width: 200 },
        { field: 'Style_Vendor', headerName: 'Vendor', width: 150 },
        { field: 'Colorway', headerName: 'Colorway', width: 125 },
        { field: 'Procurement', headerName: 'Procurement', width: 125 },
        { field: 'Mfg', headerName: 'Mfg', width: 125 },
        { field: 'GIPT', headerName: 'GIPT', width: 125 },
        { field: 'Comments', headerName: 'Comments', width: 125 },
        { field: 'LastUpdateDate', headerName: 'LastUpdateDate', width: 125 },
      ]);

    const EnviarDatos2 = async () => {
        try{
            var url = URL + 'Style_CustomerService_ProductType/add/1'
            const data = await fetch(url, {
              method: 'POST',
              headers: {'Content-Type':'application/json'},
              body: JSON.stringify([{
                      "id": 0,
                      "Style_ProductType": ProductType,
                      "Comments": Comments
                  }])
              }
            );
            swal({
                title: 'Shortlisted!',
                text: 'Data Updated successfully!',
                icon: 'success'
              });
            setOpen(false);
        } catch (error) {
            console.log(error); 
        }
    }
    const EnviarDatos3 = async () => {
        try{
            var url = URL + 'Style_CustomerService_Vendor/add/1'
            const data = await fetch(url, {
              method: 'POST',
              headers: {'Content-Type':'application/json'},
              body: JSON.stringify([{
                      "id": 0,
                      "Style_Vendor": Vendor,
                      "Comments": CommentsVendor
                  }])
              }
            );
            swal({
                title: 'Shortlisted!',
                text: 'Data Updated successfully!',
                icon: 'success'
              });
            setOpen(false);
        } catch (error) {
            console.log(error); 
        }
    }
    const UpdateProductType = async () =>  {
        try {
            const data = await fetch(URL + 'Style_CustomerService_ProductType/');
            const data1 = await data.json();
            setDataProductType(data1);
        } catch (error) {
            console.log(error); 
        }
    }
    const UpdateVendor = async () =>  {
        try {
            const data = await fetch(URL + 'Style_CustomerService_Vendor/');
            const data1 = await data.json();
            setDataVendor(data1);
        } catch (error) {
            console.log(error); 
        }
    }
    useEffect(() => {
        UpdateProductType();
        UpdateVendor();
    }, []);
    return (
        <div style={{ height: 625, width: '100%' }}>
            <ButtonGroup variant="outlined" aria-label="outlined primary button group">
                <Button onClick={() => setOpen(true)} variant="outlined" color="success" startIcon={<AddIcon />} >Product Type</Button>
                <Button onClick={() => setOpen2(true)} variant="outlined" color="success" startIcon={<AddIcon />} >Vendor</Button>
                <Button onClick={() => setOpen3(true)} variant="outlined" startIcon={<RefreshIcon />} > LeadTime</Button>
            </ButtonGroup>
            {rowData?
                <DataGrid 
                    style={{ height: 550, width: '100%' }} 
                    rows={rowData} 
                    columns={columns}
                    onRowClick={(x)=> setRowDataEdi(x.row)}
                />
            : false}
            <Dialog open={open} onClose={() => setOpen(false)} fullWidth maxWidth="xs" >
                <Grid component={Paper} elevation={6} square>
                    <Box sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column', alignItems: 'center',}}>
                        <Typography component="h1" variant="h5">Product Type</Typography>
                        <TextField value={ProductType} onChange={e => setProductType(e.target.value)} margin="normal" fullWidth id="ProductType" label="ProductType" name="ProductType"/>
                        <TextField value={Comments} onChange={e => setComments(e.target.value)} margin="normal" fullWidth id="Comments" label="Comments" name="Comments"/>
                        <Button onClick={EnviarDatos2} fullWidth variant="contained" color="success" endIcon={<SendIcon />}>
                            save
                        </Button>
                    </Box>
                </Grid>
            </Dialog>
            <Dialog open={open2} onClose={() => setOpen2(false)} fullWidth maxWidth="xs" >
                <Grid component={Paper} elevation={6} square>
                    <Box sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column', alignItems: 'center',}}>
                        <Typography component="h1" variant="h5">Vendor</Typography>
                        <TextField value={Vendor} onChange={e => setVendor(e.target.value)} margin="normal" fullWidth id="Vendor" label="Vendor" name="Vendor"/>
                        <TextField value={CommentsVendor} onChange={e => setCommentsVendor(e.target.value)} margin="normal" fullWidth id="CommentsVendor" label="Comments" name="CommentsVendor"/>
                        <Button onClick={EnviarDatos3} fullWidth variant="contained" color="success" endIcon={<SendIcon />}>
                            save
                        </Button>
                    </Box>
                </Grid>
            </Dialog>
            <Dialog open={open3} onClose={() => setOpen3(false)} fullWidth maxWidth="xs" >
                <Grid component={Paper} elevation={6} square>
                    <Box sx={{ my: 8, mx: 4, display: 'flex', flexDirection: 'column', alignItems: 'center',}}>
                        <Typography component="h1" variant="h5">Vendor</Typography>
                        <Autocomplete
                            fullWidth
                            margin="normal"
                            id="free-solo-demo"
                            onChange={(event, newValue) => {
                                setIDProductType(newValue);
                            }}
                            value={IDProductType}
                            options={(DataProductType)?DataProductType.map((option) =>option.id + '-' + option.Style_ProductType):[]}
                            renderInput={(params) => <TextField {...params} label="Product Type" />}
                        />
                        <br/>
                        <Autocomplete
                            fullWidth
                            id="free-solo-demo"
                            onChange={(event, newValue) => {
                                setIDVendor(newValue);
                            }}
                            value={IDVendor}
                            options={(DataVendor)?DataVendor.map((option) =>option.id + '-' + option.Style_Vendor):[]}
                            renderInput={(params) => <TextField {...params} label="Vendor" />}
                        />
                        <TextField value={StyleNumber} onChange={e => setStyleNumber(e.target.value)} margin="normal" fullWidth id="StyleNumber" label="StyleNumber" name="StyleNumber"/>
                        <TextField value={Colorway} onChange={e => setColorway(e.target.value)} margin="normal" fullWidth id="Colorway" label="Colorway" name="Colorway"/>
                        <TextField value={Procurement} onChange={e => setProcurement(e.target.value)} margin="normal" fullWidth id="Procurement" label="Procurement" name="Procurement"/>
                        <TextField value={Mfg} onChange={e => setMfg(e.target.value)} margin="normal" fullWidth id="Mfg" label="Mfg" name="Mfg"/>
                        <TextField value={GIPT} onChange={e => setGIPT(e.target.value)} margin="normal" fullWidth id="GIPT" label="GIPT" name="GIPT"/>
                        <Button onClick={EnviarDatos3} fullWidth variant="contained" color="success" endIcon={<SendIcon />}>
                            save
                        </Button>
                    </Box>
                </Grid>
            </Dialog>
        </div>
    )
}

export default CustomerData