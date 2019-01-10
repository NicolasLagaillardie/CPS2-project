function load_tab(elt)
{
    //console.log(elt.id);
    if(elt.id === 'onglet1')
    {
	if( layer1.getVisible() )
	{	    
	    layer1.setVisible(false);
	    map.removeLayer(layer1);	    
	}
	else
	{
	    if(map.getView().getResolution() > 1)
	    {
		layer1 = createLayerSensorCluster('sensorbase_4');
	    }
	    else
	    {
		layer1 = createLayerSensor('sensorbase_4');
	    }
	    map.addLayer(layer1);
	    layer1.setVisible(true);
	}
	return;
    }
    if(elt.id === 'onglet2')
    {
	if( layer2.getVisible() )
	{
	    layer2.setVisible(false);
	    map.removeLayer(layer2);
	}
	else
	{
	    layer2 = createLayerOffice('office_4');
	    map.addLayer(layer2);
	    layer2.setVisible(true);
	}
	return;
    }    
}
