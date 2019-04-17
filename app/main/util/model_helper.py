""" Model Helper """
from ..models.price import Price as PriceModel


def get_or_create(session, model, **kwargs):
    """ Find or Create by """

    instance = session.query(model).filter_by(**kwargs).first()
    if instance:
        return instance
    else:
        instance = model(**kwargs)
        session.add(instance)
        session.commit()
        return instance


def get_latest_date():
    """ Gets the latest date """

    latest_date = PriceModel.query.order_by(PriceModel.id.desc()).first().date
    return latest_date.strftime('%Y-%m-%d')
