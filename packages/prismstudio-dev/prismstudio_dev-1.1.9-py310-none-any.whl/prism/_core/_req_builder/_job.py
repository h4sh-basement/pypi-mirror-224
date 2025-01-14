from ..._common.config import *
from ..._common.const import *
from ..._utils import _validate_args, get, delete, post


__all__ = ['list_job', 'get_job', 'delete_job', 'strategy_backtest_jobs', 'factor_backtest_jobs', 'screen_jobs', 'extract_job', 'cancel_job', 'prioritise_job', 'export_data_jobs']


@_validate_args
def list_job(
    tasktype: str = None,
    jobstatus: str = None,
    startrange: str = None,
    endrange: str = None,
):
    """
    Return all jobs.

    Parameters
    ----------
    tasktype : str, {”screen”, “factor_backtest”}
        | Task type is a value from the list.

    jobstatus : str, {“Completed”, “Failed”}
        | Job status is a value from the list.

    startrange : str, default None
        | Date string to query list of jobs within the date range.

    endrage : str, default None
        | Date string to query list of jobs within the date range.

    Returns
    -------
        pandas.DataFrame
            return all queried jobs.
        Columns:
            - *jobid*
            - *jobname*
            - *jobstatus*
            - *starttime*
            - *endtime*
            - *tasktype*
            - *result*
            - *description*

    Examples
    --------
    >>> prism.list_job()
       jobid            jobname  jobstatus                starttime                  endtime         tasktype                                        result  description
    0      6  factor_backtest_6  Completed  2022-08-10 17:38:57.290  2022-08-10 17:44:24.599  factor_backtest  {'factor_backtest': {'factorbacktestid': 6}}         None
    1      5  factor_backtest_5  Completed  2022-07-31 14:28:43.679  2022-07-31 14:29:18.272  factor_backtest  {'factor_backtest': {'factorbacktestid': 5}}         None
    2      4  factor_backtest_4  Completed  2022-07-29 15:15:49.582  2022-07-29 15:16:24.828  factor_backtest  {'factor_backtest': {'factorbacktestid': 4}}         None
    3      3  factor_backtest_3  Completed  2022-07-25 09:26:24.777  2022-07-25 09:27:01.571  factor_backtest  {'factor_backtest': {'factorbacktestid': 3}}         None
    4      2  factor_backtest_2  Completed  2022-07-18 04:47:02.414  2022-07-18 04:47:43.182  factor_backtest  {'factor_backtest': {'factorbacktestid': 2}}         None
    5      1  factor_backtest_1  Completed  2022-07-05 17:19:41.197  2022-07-05 17:19:53.012  factor_backtest  {'factor_backtest': {'factorbacktestid': 1}}         None

    """
    param = {'jobstatus': jobstatus, 'tasktype': tasktype, 'startrange': startrange, 'endrange': endrange}
    return get(URL_JOBS, param)


@_validate_args
def get_job(jobid: int):
    """
    Get detail of specified job.

    Parameters
    ----------
        jobid : int
            Specify the job id.

    Returns
    -------
        data : dataframe
            | Return job detail. The columns depends on the task type of the job
            | If tasktype is factor backtest

            - *jobid*
            - *jobname*
            - *jobstatus*
            - *starttime*
            - *endtime*
            - *universeid*
            - *universepath*
            - *factorbacktestid*
            - *avg_turnover*
            - *avg_ic*
            - *top_bottom_spread*
            - *frequency*
            - *bins*
            - *max_days*
            - *rank_method*
            - *description*
            - *period*

            | If tasktype is screen

            - *jobid*
            - *jobname*
            - *jobstatus*
            - *starttime*
            - *endtime*
            - *frequency*
            - *screeneduniverseid*
            - *screeneduniversepath*
            - *universepath*
            - *universeid*
            - *description*
            - *period*

    Examples
    --------
    >>> prism.list_job()
       jobid            jobname  jobstatus                starttime                  endtime         tasktype                                        result  memo
    0      6  factor_backtest_6  Completed  2022-08-10 17:38:57.290  2022-08-10 17:44:24.599  factor_backtest  {'factor_backtest': {'factorbacktestid': 6}}  None
    1      5  factor_backtest_5  Completed  2022-07-31 14:28:43.679  2022-07-31 14:29:18.272  factor_backtest  {'factor_backtest': {'factorbacktestid': 5}}  None
    2      4  factor_backtest_4  Completed  2022-07-29 15:15:49.582  2022-07-29 15:16:24.828  factor_backtest  {'factor_backtest': {'factorbacktestid': 4}}  None
    3      3  factor_backtest_3  Completed  2022-07-25 09:26:24.777  2022-07-25 09:27:01.571  factor_backtest  {'factor_backtest': {'factorbacktestid': 3}}  None
    4      2  factor_backtest_2  Completed  2022-07-18 04:47:02.414  2022-07-18 04:47:43.182  factor_backtest  {'factor_backtest': {'factorbacktestid': 2}}  None
    5      1  factor_backtest_1  Completed  2022-07-05 17:19:41.197  2022-07-05 17:19:53.012  factor_backtest  {'factor_backtest': {'factorbacktestid': 1}}  None

    >>> prism.get_job(1)
         jobid            jobname  jobstatus  factorbacktestid  avg_turnover  avg_ic  top_bottom_spread  frequency  bins  max_days  rank_method  description                   period
    0	     1  factor_backtest_1  Completed                31      0.475282  0.0178          -0.000383          Q    10        93     standard         None  2013-01-01 ~ 2015-01-01

    """
    return get(f'{URL_JOBS}/id/{jobid}', None)


@_validate_args
def strategy_backtest_jobs():
    return get(URL_JOBS + '/type/strategy_backtest', None)


@_validate_args
def factor_backtest_jobs():
    """
    List all factor backtest jobs and their detail.

    Returns
    -------
        pandas.DataFrame
            All factor backtest jobs.
        Columns
            - *jobid*
            - *jobname*
            - *jobstatus*
            - *starttime*
            - *endtime*
            - *universeid*
            - *universepath*
            - *factorbacktestid*
            - *avg_turnover*
            - *avg_ic*
            - *top_bottom_spread*
            - *frequency*
            - *bins*
            - *max_days*
            - *rank_method*
            - *description*
            - *period*

    Examples
    --------
    >>> prism.factor_backtest_jobs()
       jobid  jobstatus                   starttime                     endtime  ...  factorbacktestid  avg_turnover     avg_ic  top_bottom_spread  frequency  bins                   period
    0	   4  Completed  2022-06-29 17:48:41.023456  2022-06-29 17:52:03.637405  ...                 4      0.854072  -0.016881          -0.000389          Q    10  2000-01-01 ~ 2020-01-01
    1      3  Completed  2022-06-29 10:22:29.928233  2022-06-29 10:22:35.714741  ...                 3      0.388650  -0.009124          -0.000291          M     5  2015-01-01 ~ 2020-12-31
    2      2  Completed  2022-06-29 08:55:55.268231  2022-06-29 08:56:03.530062  ...                 2      0.380334  -0.022625          -0.000524          M     5  2015-01-01 ~ 2020-12-31
    3      1  Completed  2022-06-27 18:08:36.775176  2022-06-27 18:09:00.530742  ...                 1      0.879670  -0.074594          -0.000771          Q    10  2010-01-01 ~ 2011-01-01
    """
    return get(URL_JOBS + '/type/factor_backtest', None)


@_validate_args
def screen_jobs():
    """
    List all screen jobs.

    Returns
    -------
        pandas.DataFrame
            All screen jobs.
        Columns
            - *jobid*
            - *jobname*
            - *jobstatus*
            - *starttime*
            - *endtime*
            - *frequency*
            - *screeneduniverseid*
            - *screeneduniversepath*
            - *universepath*
            - *universeid*
            - *description*
            - *period*

    Examples
    --------
    >>> prism.screen_jobs()
       jobid  jobname  jobstatus                starttime                        endtime  frequency  screeneduniverseid  ...  universeid  description                   period
    0      1     None  Completed  2022-06-30 03:51:13.630  2022-06-30 03:51:18.388999936          Q                 9.0  ...         7.0         None  2010-01-01 ~ 2015-01-01
    1      2     None  Completed  2022-06-30 03:49:24.680  2022-06-30 03:49:28.556000000          Q                 8.0  ...	     7.0         None  2010-01-01 ~ 2015-01-01
    2      3     None  Completed  2022-06-27 17:37:27.386  2022-06-27 17:37:51.248000000          Q                 9.0  ...         7.0         None  2010-01-01 ~ 2015-01-01
    """
    return get(URL_JOBS + '/type/screen', None)


@_validate_args
def export_data_jobs():
    """
    List all export_data jobs.
    """
    return get(URL_JOBS + '/type/export_data', None)


@_validate_args
def delete_job(jobid: int):
    """
    Delete job with job id.

    Parameters
    ----------
        jobid : int
            Specify job id to be deleted.

    Returns
    -------
        status : dict
            Status of delete_job.

    Examples
    --------
    >>> prism.list_job()
       jobid            jobname  jobstatus                starttime                  endtime         tasktype                                        result  description
    0      6  factor_backtest_6  Completed  2022-08-10 17:38:57.290  2022-08-10 17:44:24.599  factor_backtest  {'factor_backtest': {'factorbacktestid': 6}}         None
    1      5  factor_backtest_5  Completed  2022-07-31 14:28:43.679  2022-07-31 14:29:18.272  factor_backtest  {'factor_backtest': {'factorbacktestid': 5}}         None
    2      4  factor_backtest_4  Completed  2022-07-29 15:15:49.582  2022-07-29 15:16:24.828  factor_backtest  {'factor_backtest': {'factorbacktestid': 4}}         None
    3      3  factor_backtest_3  Completed  2022-07-25 09:26:24.777  2022-07-25 09:27:01.571  factor_backtest  {'factor_backtest': {'factorbacktestid': 3}}         None
    4      2  factor_backtest_2  Completed  2022-07-18 04:47:02.414  2022-07-18 04:47:43.182  factor_backtest  {'factor_backtest': {'factorbacktestid': 2}}         None
    5      1  factor_backtest_1  Completed  2022-07-05 17:19:41.197  2022-07-05 17:19:53.012  factor_backtest  {'factor_backtest': {'factorbacktestid': 1}}         None

    >>> prism.delete_job(1)
    {
    'status': 'Success',
    'message': 'Job deleted',
    'result': [{'resulttype': 'jobid', 'resultvalue': 1}]
    }

    >>> prism.list_job()
       jobid            jobname  jobstatus                starttime                  endtime         tasktype                                        result  description
    0      6  factor_backtest_6  Completed  2022-08-10 17:38:57.290  2022-08-10 17:44:24.599  factor_backtest  {'factor_backtest': {'factorbacktestid': 6}}         None
    1      5  factor_backtest_5  Completed  2022-07-31 14:28:43.679  2022-07-31 14:29:18.272  factor_backtest  {'factor_backtest': {'factorbacktestid': 5}}         None
    2      4  factor_backtest_4  Completed  2022-07-29 15:15:49.582  2022-07-29 15:16:24.828  factor_backtest  {'factor_backtest': {'factorbacktestid': 4}}         None
    3      3  factor_backtest_3  Completed  2022-07-25 09:26:24.777  2022-07-25 09:27:01.571  factor_backtest  {'factor_backtest': {'factorbacktestid': 3}}         None
    4      2  factor_backtest_2  Completed  2022-07-18 04:47:02.414  2022-07-18 04:47:43.182  factor_backtest  {'factor_backtest': {'factorbacktestid': 2}}         None

    """
    ret = delete(URL_JOBS + f'/{jobid}')
    return ret


@_validate_args
def cancel_job(jobid: int):
    """
    Cancel specified job.

    Parameters
    ----------
        jobid : int
            Specify the job id.

    Returns
    -------
        Result of canceled job.

    Examples
    --------
    >>> ep = prism.financial.income_statement(100723, 'Q').resample(frequency='M', lookback=30) / prism.market.market_cap().resample('M', lookback=30)
    >>> prism.factor_backtest(ep, 'Korea_primary', 'M', 10, '2015-01-01').run('ep_df')
    factor_backtest is added to worker queue!: jobid is 321

    >>> prism.cancel_job(321)
    {
        'status': 'Canceled',
        'message': 'screen is deleted from queue!',
        'result': []
    }
    """
    ret = delete(URL_TASK + f'/revoke/{jobid}')
    return ret


@_validate_args
def prioritise_job(jobid: int):
    """
    Prioritise specified job.

    Parameters
    ----------
        jobid : int
            Specify the job id.

    Returns
    -------
        Result of prioritized job.


    Examples
    --------
    >>> ep = prism.financial.income_statement(100723, 'Q').resample(frequency='M', lookback=30) / prism.market.market_cap().resample('M', lookback=30)
    >>> prism.factor_backtest(ep, 'Korea_primary', 'M', 10, '2015-01-01').run('ep_df')
    factor_backtest is added to worker queue!: jobid is 321

    >>> prism.prioritise_job(321)
    {
        'status': 'Success',
        'message': 'factor backtest is prioritised in the queue!',
        'result': []
    }
    """
    ret = post(URL_TASK + f'/prioritise/{jobid}')
    return ret


@_validate_args
def extract_job(jobid: int, return_code=False):
    """
    Generate code which reproduces the taskquery which runs the job specified by the jobid. If return_code is False, the method returns None and prints the code.

    Parameters
    ----------
        jobid : int
            | Job id whose taskquery is to be extracted.

        return_code : bool, default False
            | if True, the method returns the code. Else the code is printed as system output, returning None.

    Returns
    -------
        return_code = True
            code: str

        return_code = False
            None

    Examples
    --------
    >>> ni = prism.financial.income_statement(100639, periodtype="LTM")
    >>> mcap = prism.market.market_cap()
    >>> ep = ni / mcap
    >>> ep_fb = prism.factor_backtest(factor=ep, universe="S&P 500", startdate="2013-01-01", enddate="2015-01-01", frequency="Q", bins=10)
    >>> ep_fb.run()
    Done!
    factor_backtest Completed: factorbacktestid is 1
    Fetching A Link to Factor Backtest Report...
    Link to Factor Backtest Report:
    https://ext.prism39.com/report/factor_backtest/my_username_1_96cebcc1-fe3d-4de7-b433-e32d6fcc13c9/

    >>> prism.extract_job(jobid=1)
    x0 = prism.financial.income_statement(dataitemid=100639, periodtype="LTM", package="CIQ Premium Financials", preliminary=True, currency=None)
    x1 = prism.market.marketcap(currency=None, package="CIQ Market")
    x2 = x0 / x1
    x3 = prism.factor_backtest(factor=x2, universe=2, startdate="2013-01-01", enddate="2015-01-01", frequency="Q", bins=10, rank_method="standard", max_days=None)
    """
    code = get(URL_JOBS + f'/extract/{jobid}', {'dialect': 'python'})
    if return_code:
        return code
    else:
        print(code)


@_validate_args
def rename_job(jobid: int, jobname: str):
    return post(URL_JOBS + f'/jobname/{jobid}', body=jobname)


@_validate_args
def add_job_description(jobid: int, description: str):
    return post(URL_JOBS + f'/description/{jobid}', body=description)