import React, {useState} from 'react';

import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import Collapse from '@mui/material/Collapse';
import ExpandLess from '@mui/icons-material/ExpandLess';
import ExpandMore from '@mui/icons-material/ExpandMore';
import CloudUploadIcon from '@mui/icons-material/CloudUpload';
import UploadFileIcon from '@mui/icons-material/UploadFile';
import AssessmentIcon from '@mui/icons-material/Assessment';
import PieChartIcon from '@mui/icons-material/PieChart';
import StyleIcon from '@mui/icons-material/Style';
import GroupsIcon from '@mui/icons-material/Groups';
import ScheduleIcon from '@mui/icons-material/Schedule';
import AccountTreeIcon from '@mui/icons-material/AccountTree';
import { useNavigate } from 'react-router-dom';


function ListItem() {
    const navigate = useNavigate();
    const [open, setOpen] = useState(true);
    const [open2, setOpen2] = useState(true);
    const [open3, setOpen3] = useState(true);
    const [open4, setOpen4] = useState(true);
    const handleClick = () => {
      setOpen(!open);
    };
    const handleClick2 = () => {
        setOpen2(!open2);
    };
    const handleClick3 = () => {
    setOpen3(!open3);
    };
    const handleClick4 = () => {
        setOpen4(!open4);
        };
    return (
    <React.Fragment>
        <ListItemButton onClick={handleClick}>
            <ListItemIcon>
            <CloudUploadIcon />
            </ListItemIcon>
            <ListItemText primary="Upload" />
            {open ? <ExpandLess /> : <ExpandMore />}
        </ListItemButton>
        <Collapse in={open} timeout="auto" unmountOnExit>
            <List onClick={() => navigate('/Main/PromisedDate')} component="div" disablePadding>
                <ListItemButton sx={{ pl: 4 }}>
                    <ListItemIcon>
                    <UploadFileIcon />
                    </ListItemIcon>
                    <ListItemText primary="Promised Date" />
                </ListItemButton>
            </List>
            <List onClick={() => navigate('/Main/StyleBroad')} component="div" disablePadding>
                <ListItemButton sx={{ pl: 4 }}>
                    <ListItemIcon>
                    <UploadFileIcon />
                    </ListItemIcon>
                    <ListItemText primary="DataBase Style" />
                </ListItemButton>
            </List>
        </Collapse>
        <ListItemButton onClick={handleClick2}>
            <ListItemIcon>
            <AssessmentIcon />
            </ListItemIcon>
            <ListItemText primary="Power Bi" />
            {open2 ? <ExpandLess /> : <ExpandMore />}
        </ListItemButton>
        <Collapse in={open2} timeout="auto" unmountOnExit>
            <List onClick={() => navigate('/Main/CAPlanning')} component="div" disablePadding>
                <ListItemButton sx={{ pl: 4 }}>
                    <ListItemIcon>
                    <PieChartIcon />
                    </ListItemIcon>
                    <ListItemText primary="CA Planning Dash" />
                </ListItemButton>
            </List>
        </Collapse>
        <ListItemButton onClick={handleClick3}>
            <ListItemIcon>
                <StyleIcon />
            </ListItemIcon>
            <ListItemText primary="Database Style" />
            {open3 ? <ExpandLess /> : <ExpandMore />}
        </ListItemButton>
        <Collapse in={open3} timeout="auto" unmountOnExit>
            <List onClick={() => navigate('/Main/CustomerData')} component="div" disablePadding>
                <ListItemButton sx={{ pl: 4 }}>
                    <ListItemIcon>
                        <GroupsIcon />
                    </ListItemIcon>
                    <ListItemText primary="Customer Service" />
                </ListItemButton>
            </List>
        </Collapse>
        <ListItemButton onClick={handleClick4}>
            <ListItemIcon>
                <AccountTreeIcon />
            </ListItemIcon>
            <ListItemText primary="Supply Planning" />
            {open4 ? <ExpandLess /> : <ExpandMore />}
        </ListItemButton>
        <Collapse in={open4} timeout="auto" unmountOnExit>
            <List onClick={() => navigate('/Main/SupplyCycle')} component="div" disablePadding>
                <ListItemButton sx={{ pl: 4 }}>
                    <ListItemIcon>
                        <ScheduleIcon />
                    </ListItemIcon>
                    <ListItemText primary="Cycle" />
                </ListItemButton>
            </List>
        </Collapse>
    </React.Fragment>
  )
}

export default ListItem