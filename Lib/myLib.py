def pandas_to_seaborn_prep(df,columns, add_columns = None, normalize = False):
    """
    Preprocess Pandas DataFrame for plotting with Seaborn
    Arguments:
        df: Pandas DataFrame object
        columns: list of the columns of the DataFrame to plot
        add_columns: additional columns to pass 
        normalize: option to normalize the values (-1,1) 
    Returns:
        a Pandas DataFrame object with the columns stacked one onto the other. 
        The values are stored in a column "Values" and the column names in a column "Features".
        If a add_columns is given, they will be stored in columns having the same name as the original DataFrame 
    """
    
    import sys
    if 'pd' not in sys.modules:
        raise ImportError("Module Pandas not found, please import it as pd")
    
    
    if add_columns is not None:
        columns_plot = ["Values","Features"].append(add_columns) 
    else:
        columns_plot = ["Values","Features"]
        
    df_plot = pd.DataFrame(columns = columns_plot)

    if normalize is True:
        df[columns] = df[columns]/(df[columns].max())     
            
    for col in columns:
        df_temp = pd.DataFrame()
        df_temp["Values"] = df[col].values
        if add_columns is not None:
            for add_col in add_columns:
                df_temp[add_col] = df[add_col].values
        df_temp["Features"] = col
        df_plot = pd.concat([df_plot,df_temp],ignore_index = True)
        del df_temp
        
    return(df_plot)